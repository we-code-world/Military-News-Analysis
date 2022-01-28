package Tools;

import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Font;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.BaseFont;
import com.lowagie.text.pdf.PdfWriter;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import static org.apache.commons.lang.StringUtils.leftPad;

public class CreatePDF{
    public static void createPdfFile(String fileName) throws IOException, DocumentException {
        Document document = new Document();
        //add Chinese font
        BaseFont bfChinese=BaseFont.createFont();

        //Font headfont=new Font(bfChinese,10,Font.BOLD);
        Font keyfont=new Font(bfChinese,8, Font.BOLD);
        try {
            File file = new File(fileName);
            if(!file.exists()){
                boolean fr = file.createNewFile();
                if (!fr)return;
            }
            FileOutputStream fileOutputStream = new FileOutputStream(file);
            PdfWriter.getInstance(document, fileOutputStream);
            document.open();
            String pageNo=leftPad("页码: "+(1)+" / "+1,615);
            Paragraph pageNumber=new Paragraph(pageNo, keyfont) ;
            document.add(pageNumber);
            document.close();
        } catch (IOException | DocumentException e) {
            e.printStackTrace();
        }
    }
    public static boolean delPdfFile(String fileName) throws IOException {
        File file = new File(fileName);
        if(!file.exists()){
            return true;
        }
        return file.delete();
    }
}
