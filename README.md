graph TD
    subgraph 控制平面 (Control Plane)
        APIServer[Kubernetes API Server]
        Scheduler[Kubernetes Scheduler]
    end

    subgraph 数据平面 (Data Plane)
        Kubelet[Kubelet]
        DRA_Driver[DRA Driver (你的 Agent)]
        GPU_HW[底层 GPU 硬件]
    end

    subgraph 开发者 & 用户 (Developer & User)
        User[用户 (提交 Pod)]
    end

    User --> |1. 提交 Pod, ResourceClaim| APIServer
    DRA_Driver --> |2a. 驱动启动时提交| APIServer
    DRA_Driver --> |2b. 持续更新| APIServer
    APIServer --> |3. 通知 Scheduler 新建 Pod| Scheduler
    Scheduler --> |4. 查询 ResourceSlice, 找到节点| APIServer
    Scheduler --> |5. 绑定 ResourceClaim, 更新 Pod| APIServer
    APIServer --> |6. 通知 Kubelet 运行 Pod| Kubelet
    Kubelet --> |7. 调用本地 DRA 驱动, 请求分配| DRA_Driver
    DRA_Driver --> |8a. 获取底层 GPU 信息| GPU_HW
    DRA_Driver --> |8b. 执行分配逻辑| DRA_Driver
    DRA_Driver --> |9. 返回设备信息 (设备路径, 环境变量)| Kubelet
    Kubelet --> |10. 配置 CRI, 启动容器| Kubelet
    GPU_HW --> |8a. 返回 GPU 信息 (显存, ID)| DRA_Driver

    subgraph 交互详情 (Interaction Details)
        style APIServer fill:#f9f,stroke:#333,stroke-width:2px
        style Scheduler fill:#b9f,stroke:#333,stroke-width:2px
        style Kubelet fill:#bbf,stroke:#333,stroke-width:2px
        style DRA_Driver fill:#ffa,stroke:#333,stroke-width:2px
        style GPU_HW fill:#fbb,stroke:#333,stroke-width:2px
        style User fill:#afa,stroke:#333,stroke-width:2px

        APIServer -- CRUD (ResourceClass, ResourceSlice) --> DRA_Driver
        APIServer -- CRUD (ResourceClaim) --> User
        Scheduler -- 查询 (ResourceSlice) --> APIServer
        Scheduler -- 更新 (ResourceClaim) --> APIServer
        Kubelet -- gRPC Allocate() --> DRA_Driver
        DRA_Driver -- 命令/SDK --> GPU_HW
        Kubelet -- CRI 配置 --> Pod[Pod]
    end
