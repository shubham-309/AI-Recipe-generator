# AI Recipe Generator

## Overview
The **AI Recipe Generator** is a web-based application that creates unique and delicious recipes based on user inputs. Users can either provide a list of ingredients as text or upload an image (e.g., of their refrigerator or pantry), and the app will generate a detailed, step-by-step recipe. Powered by Google’s Gemini 1.5 Flash model, LangChain, and Streamlit, this app offers a seamless and innovative cooking experience.

## Features
- **Text Input Mode**: Enter a list of ingredients to receive a tailored recipe with preparation steps, cooking techniques, and garnish suggestions.
- **Image Input Mode**: Upload an image, and the AI identifies ingredients to create a customized recipe.
- **Dietary Considerations**: Recipes can accommodate dietary preferences (e.g., vegetarian, vegan) based on the prompt design.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and responsive experience.
- **Creative Suggestions**: Includes tips for flavor enhancement and ingredient substitutions.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python, LangChain, Google Gemini 1.5 Flash
- **Image Processing**: PIL (Python Imaging Library)
- **Environment Management**: python-dotenv
- **APIs**: Google Generative AI

## Installation

### Prerequisites
- Python 3.8+
- pip
- A Google API key for Gemini (set up in a `.env` file)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai-recipe-generator.git
   cd ai-recipe-generator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the project root and add your Google API key:
   ```env
   GOOGLE_API_KEY=your-api-key-here
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   Open your browser and navigate to `http://localhost:8501`.

## Usage
1. **Text Input**:
   - Select the "Text Input" option.
   - Enter a comma-separated list of ingredients (e.g., "rice, peppers, tomatoes, lentils").
   - Click "Generate" to view the recipe.

2. **Image Input**:
   - Select the "Image Input" option.
   - Upload a `.jpg`, `.jpeg`, or `.png` image of your ingredients.
   - Click "Generate Recipe" to see the AI-generated recipe based on the image.

## File Structure
```
ai-recipe-generator/
├── app.py                  # Main application script
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not tracked)
├── README.md               # This file
└── .gitignore              # Git ignore file
```

## Dependencies
Listed in `requirements.txt`:
```
streamlit
python-dotenv
langchain
langchain-google-genai
google-generativeai
pillow
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Future Enhancements
- Add dietary preference filters (e.g., vegetarian, gluten-free).
- Implement user confirmation for detected ingredients in images.
- Enable recipe export as PDF or sharing via email/social media.
- Support multilingual recipe generation.
- Integrate with grocery delivery APIs for ingredient suggestions.

## Troubleshooting
- **API Key Issues**: Ensure your Google API key is correctly set in the `.env` file.
- **Image Processing Errors**: Verify that uploaded images are in supported formats (`.jpg`, `.jpeg`, `.png`).
- **API Rate Limits**: If you encounter rate limit errors, consider caching responses or upgrading your API plan.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, reach out via [email@example.com](mailto:email@example.com) or open an issue on GitHub.

---
Built with ❤️ by Shubham
