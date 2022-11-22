#convert images to pdf
#pip3 install fpdf

from fpdf import FPDF

pdf  = FPDF()

#image list is the list ith all image filenames
for image in imagelist:
        pdf.add_page()
        pdf.image(image,x,y,w,h)
        pdf.output("image2pdf.pdf", "F")