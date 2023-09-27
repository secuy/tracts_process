import numpy as np

from dipy.io.streamline import load_trk, load_tck
from dipy.data.fetcher import fetch_file_formats, get_file_formats
import nibabel as nib


def get_tck_streamlines(filename):
    fetch_file_formats()
    bundles_filename, ref_anat_filename = get_file_formats()
    references = nib.load(ref_anat_filename)

    path_tck = filename
    streamlines = load_tck(path_tck, reference=references, bbox_valid_check=False).streamlines

    return streamlines

def get_trk_streamlines(filename):
    fetch_file_formats()
    bundles_filename, ref_anat_filename = get_file_formats()
    references = nib.load(ref_anat_filename)

    path_trk = filename
    streamlines = load_trk(path_trk, reference="same", bbox_valid_check=False).streamlines

    return streamlines
