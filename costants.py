import os

THREADS = 8

# 1. Read pdf and extract images from it

#TEST_PDF_PATH = os.path.join('pdf/polizze/alupress_cropped.pdf')
#TEST_PDF_PATH = os.path.join('pdf/polizze/unipol_rischi_industriali.pdf')
#TEST_PDF_PATH = os.path.join('pdf/polizze/unipol_all_risks_property_cropped10.pdf')
TEST_PDF_PATH = os.path.join('pdf/polizze/piovan_property4.pdf')

# store here temporary images made by splitting the pdf in singular image files
TEMP_IMG_FOLDER_FROM_PDF = 'tmp'

# extracted images are put in PATH_TO_EXTRACTED_IMAGES. Images quality is: EXTRACTION_DPI = 300
PATH_TO_EXTRACTED_IMAGES = 'extracted_images' # set to - None - if you don't want any
EXTRACTION_DPI = 300


# 2. Find tables and text inside page. Script: find_table.py
# inference graphs

INFERENCE_GRAPH = 'inference_graphs/frozen_adam2_tb/frozen_inference_graph.pb'

# table.py uses these constants:
MAX_NUM_BOXES = 10
MIN_SCORE = 0.7


# 3. Extract tables from table images
TABLE_FOLDER = 'table'
TEST_TABLE_PATH = os.path.join('extracted_images/sample1')

# 4. Extract text from text images
TEXT_FOLDER = 'text'
