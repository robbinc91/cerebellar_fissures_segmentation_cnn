input_dir = '..\\images\\'
output_dir = '..\\images\\'

# Processing all images
imgs = [i for i in range(31, 55)]

from skimage.filters import threshold_otsu
from skimage.segmentation import chan_vese, active_contour



def _chan_vese(data):
    for slice_index in range(data.shape[2]):
        data[:, :, slice_index] = chan_vese(data[:, :, slice_index])
        
    return data


def _active_contour(data):
    for slice_index in range(data.shape[2]):
        data[:, :, slice_index] = active_contour(data[:, :, slice_index])
        
    return data


def histogramequalization():
    for i in imgs:
        nm = 'a{:02d}'.format(i)
        input_name = '{0}{1}_n4_mni.nii.gz'.format(input_dir, nm)
        output_name = '{0}{1}-histeq.nii.gz'.format(input_dir, nm)
        img = nib.load(input_name)
               
        dta = img.get_data()
        #dta = skull_strip(dta)
		# We tested skull stripping from deepbrain but we decided not to use it
        
        dta = histeq(to_uint8(normalize(dta)))       
        _val = dta.std()
        
        dta = dta > threshold_otsu(dta)
        dta = scipy.ndimage.binary_fill_holes(dta).astype(np.uint8)
        imgoutput = nib.Nifti1Image(dta, affine=img.affine)
        imgoutput.to_filename(output_name)
                
histogramequalization()

