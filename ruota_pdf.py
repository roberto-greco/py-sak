import PyPDF2
import sys

def ruota_pdf(input_path, output_path, gradi):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for pagina in range(len(pdf_reader.pages)):
            pagina_corrente = pdf_reader.pages[pagina]
            pagina_corrente.rotate(gradi)
            pdf_writer.add_page(pagina_corrente)

        with open(output_path, 'wb') as file_output:
            pdf_writer.write(file_output)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file rotation_angle")
        sys.exit(1)

    # Ottieni i nomi dei file e l'angolo di rotazione dagli argomenti della riga di comando
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    angolo_rotazione = int(sys.argv[3])

    # Chiama la funzione per ruotare il PDF
    ruota_pdf(input_path, output_path, angolo_rotazione)
