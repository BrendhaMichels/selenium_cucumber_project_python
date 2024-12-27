from fpdf import FPDF
import os
from selenium import webdriver
from datetime import datetime
from PIL import Image

def before_all(context):
    context.test_results = []  # Lista para armazenar os resultados dos testes
    context.screenshots_dir = "screenshots"
    os.makedirs(context.screenshots_dir, exist_ok=True)  # Criar diretório para capturas de tela
    print("Starting tests...")

def after_step(context, step):
    # Capturar screenshots após cada passo
    if hasattr(context, "driver"):  # Verifica se o WebDriver está disponível
        screenshot_path = os.path.join(
            context.screenshots_dir,
            f"{step.name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        )
        context.driver.save_screenshot(screenshot_path)
        # Adicionar o caminho do screenshot ao resultado do passo
        context.test_results.append({
            "step": step.name,
            "status": "PASSED" if step.status == "passed" else "FAILED",
            "screenshot": screenshot_path
        })

def after_scenario(context, scenario):
    # Adicionar o resultado do cenário
    context.test_results.append({
        "scenario": scenario.name,
        "status": "PASSED" if scenario.status == "passed" else "FAILED",
    })

def after_all(context):
    # Gerar o relatório em PDF
    generate_pdf_report(context.test_results, context.screenshots_dir)
    print("All tests completed!")
    if hasattr(context, "driver"):
        context.driver.quit()

def generate_pdf_report(test_results, screenshots_dir):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do relatório
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Test Execution Report with Screenshots", ln=True, align="C")
    pdf.ln(10)

    # Corpo do relatório
    pdf.set_font("Arial", size=12)
    current_scenario = None

    for result in test_results:
        # Exibir título do cenário
        if "scenario" in result:
            current_scenario = result["scenario"]
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(0, 10, txt=f"Scenario: {current_scenario}", ln=True)
            continue

        # Exibir passos e capturas de tela
        step = result.get("step")
        status = result.get("status")
        screenshot = result.get("screenshot")

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"Step: {step} - Status: {status}", ln=True)

        # Adicionar captura de tela ao PDF
        if screenshot and os.path.exists(screenshot):
            pdf.image(screenshot, x=10, y=pdf.get_y(), w=100)
            pdf.ln(60)  # Ajustar o espaçamento para a próxima entrada

    # Salvar o relatório como PDF
    pdf.output("test_report_with_screenshots.pdf")
    print("PDF report with screenshots generated: test_report_with_screenshots.pdf")
