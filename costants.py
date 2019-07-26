import os

THREADS = 8

# 1. Read pdf and extract images from it

# TEST_PDF_PATH = os.path.join('C:/Users/giova/Documents/PycharmProjects/Polizze/glossario.pdf')
TEST_PDF_PATH = os.path.join('pdf/sample1.pdf')
# store here temporary images made by splitting the pdf in singular image files
TEMP_IMG_FOLDER_FROM_PDF = 'pdf_temp'

# extracted images are put in PATH_TO_EXTRACTED_IMAGES. Images quality is: EXTRACTION_DPI = 300
PATH_TO_EXTRACTED_IMAGES = 'extracted_images' # set to - None - if you don't want any
EXTRACTION_DPI = 300


# 2. Find tables and text inside page. Script: find_table.py
# inference graphs
inference_graph_momentum = \
    os.path.join(
        '/home/iaito/git/TableTrainNet/trained_models/model__rcnn_inception_adam_1/frozen/frozen_inference_graph_momentum.pb')

inference_graph_adam_3 = \
    os.path.join('/home/iaito/git/TableTrainNet/trained_models/'
                 'model__rcnn_inception_adam_3/frozen/frozen_inference_graph.pb')

INFERENCE_GRAPH = inference_graph_adam_3

# table.py uses these constants:
MAX_NUM_BOXES = 10
MIN_SCORE = 0.4


# 3. Extract tables from table images
TABLE_FOLDER = 'table'
#TEST_TABLE_PATH = os.path.join('table/glossario/table_pag_0_0.jpeg')
TEST_TABLE_PATH = os.path.join('extracted_images/sample1')

# 4. Extract text from text images
TEXT_FOLDER = 'text'


# alupress_polizza_completa =
# os.path.join('C:/Users/giova/Documents/PycharmProjects/Polizze/polizza Alupress/ALUPRESS POLIZZA COMPLETA rev. MM 2018.pdf')
# agbra_polizza_incendio = os.path.join('C:/Users/giova/Documents/PycharmProjects/Polizze/Polizza AGBA/AGBA pol INCENDIO.pdf')

# constants used by 'find_table.py'
