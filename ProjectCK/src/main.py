# main.py
from src.predictor import predict_animal
from src.wiki_fetcher import get_wikipedia_summary
import gradio as gr

def process_image(image):
    label = predict_animal(image)
    info = get_wikipedia_summary(label)
    return f"### Dự đoán: {label}\n\n{info}"

demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Markdown(),
    title="🐾 AI Nhận Diện Loài Động Vật",
    description="Tải lên hình ảnh loài động vật để nhận diện và tra cứu thông tin."
)

if __name__ == "__main__":
    demo.launch()
