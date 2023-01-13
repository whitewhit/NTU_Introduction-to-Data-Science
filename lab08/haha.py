import fingerprint_feature_extractor
from skimage import io

if __name__ == '__main__':
    img = io.imread('Fingerprint.tif', as_gray=True)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=True, saveResult = True)