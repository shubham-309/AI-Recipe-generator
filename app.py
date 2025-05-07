from dotenv import load_dotenv
import streamlit as st 
from PIL import Image
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.llms import OpenAI

load_dotenv()

llm_g = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature = 0.9)
llm = OpenAI(temperature = 0.9) 

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    


prompt_template = PromptTemplate(
    template = "Generate a unique and delicious recipe using the following set of ingredients: {ingredients}. Craft a step-by-step cooking guide, including instructions on preparation, cooking techniques, and any additional seasonings or garnishes. Be creative and provide tips for enhancing flavors. Consider dietary preferences or restrictions if specified. Feel free to suggest variations or substitutions to accommodate different tastes." ,
    input_variables = ['ingredients'])
#template = prompt_template.format(ingredients = "rice, peppers, tomotos, lentils")

recipe_chain = LLMChain(
    llm = llm_g,
    prompt = prompt_template,
    verbose = True
)

input_prompt = "Generate a unique and delicious recipe based on the ingredients identified in the user-uploaded image data. Analyze the image to recognize the ingredients, and provide a step-by-step cooking guide. Include details on preparation, cooking techniques, and any additional seasonings or garnishes inspired by the image. Consider dietary preferences or restrictions if visible, and suggest variations or substitutions. Craft a comprehensive recipe that brings the essence of the uploaded image to the dining table."

def get_gemini_response(image,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([image[0],prompt])
    return response.text


st.title("Recipe Generator")

select = st.radio('Select one:', [1, 2])
if select == 1:
    ingredient = st.text_input("Enter list of all ingredients:- ")

    button = st.button("Genetate")
    if button and ingredient:
        with st.spinner("generating.."):
            output = recipe_chain.run(ingredients = ingredient)
            st.write(output)


if select == 2:
    upload_img = st.file_uploader("Select an image.....", type = ["jpg", "jpeg", "png"])
    image =""
    if upload_img is not None:
        image = Image.open(upload_img)
        st.image(image, use_column_width = True)

    submit = st.button("Generate Recipe")

    if submit and upload_img:
        with st.spinner("Let's cook something good.."):
            image_data = input_image_setup(upload_img)
            response=get_gemini_response(image_data, input_prompt)
            st.subheader("The Response is")
            st.write(response)
