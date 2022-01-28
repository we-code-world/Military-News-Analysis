package Tools;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.io.*;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

import org.apache.tools.zip.ZipEntry;
import org.apache.tools.zip.ZipFile;
import org.apache.tools.zip.ZipOutputStream;

public class FileIO {
    /**
     * 以字节为单位读取文件，常用于读二进制文件，如图片、声音、影像等文件。
     */
    public static void readFileByBytes(String fileName) {
        File file = new File(fileName);
        InputStream in = null;
        try {
            System.out.println("以字节为单位读取文件内容，一次读一个字节：");
            // 一次读一个字节
            in = new FileInputStream(file);
            int tempbyte;
            while ((tempbyte = in.read()) != -1) {
                System.out.write(tempbyte);
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        try {
            System.out.println("以字节为单位读取文件内容，一次读多个字节：");
            // 一次读多个字节
            byte[] tempbytes = new byte[100];
            int byteread = 0;
            in = new FileInputStream(fileName);
            FileIO.showAvailableBytes(in);
            // 读入多个字节到字节数组中，byteread为一次读入的字节数
            while ((byteread = in.read(tempbytes)) != -1) {
                System.out.write(tempbytes, 0, byteread);
            }
        } catch (Exception e1) {
            e1.printStackTrace();
        } finally {
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e1) {
                }
            }
        }
    }

    /**
     * 以字符为单位读取文件，常用于读文本，数字等类型的文件
     */
    public static void readFileByChars(String fileName) {
        File file = new File(fileName);
        Reader reader = null;
        try {
            System.out.println("以字符为单位读取文件内容，一次读一个字节：");
            // 一次读一个字符
            reader = new InputStreamReader(new FileInputStream(file));
            int tempchar;
            while ((tempchar = reader.read()) != -1) {
                // 对于windows下，\r\n这两个字符在一起时，表示一个换行。
                // 但如果这两个字符分开显示时，会换两次行。
                // 因此，屏蔽掉\r，或者屏蔽\n。否则，将会多出很多空行。
                if (((char) tempchar) != '\r') {
                    System.out.print((char) tempchar);
                }
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            System.out.println("以字符为单位读取文件内容，一次读多个字节：");
            // 一次读多个字符
            char[] tempchars = new char[30];
            int charread = 0;
            reader = new InputStreamReader(new FileInputStream(fileName));
            // 读入多个字符到字符数组中，charread为一次读取字符数
            while ((charread = reader.read(tempchars)) != -1) {
                // 同样屏蔽掉\r不显示
                if ((charread == tempchars.length)
                        && (tempchars[tempchars.length - 1] != '\r')) {
                    System.out.print(tempchars);
                } else {
                    for (int i = 0; i < charread; i++) {
                        if (tempchars[i] == '\r') {
                            continue;
                        } else {
                            System.out.print(tempchars[i]);
                        }
                    }
                }
            }

        } catch (Exception e1) {
            e1.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                }
            }
        }
    }

    /*
    *解析文件编码格式
    *@param path
    *@return
    */
    public static String resolveCode(String path) throws Exception {
//      String filePath = "D:/article.txt"; //[-76, -85, -71]  ANSI
//      String filePath = "D:/article111.txt";  //[-2, -1, 79] unicode big endian
//      String filePath = "D:/article222.txt";  //[-1, -2, 32]  unicode
//      String filePath = "D:/article333.txt";  //[-17, -69, -65] UTF-8
        InputStream inputStream = new FileInputStream(path);
        byte[] head = new byte[3];
        inputStream.read(head);
//        System.out.println(head);
        String code = "gb2312";  //或GBK
        if (head[0] == -1 && head[1] == -2 )
            code = "UTF-16";
        else if (head[0] == -2 && head[1] == -1 )
            code = "Unicode";
        else if(head[0]==-17 && head[1]==-69 && head[2] ==-65)
            code = "UTF-8";
        else code = "UTF-8";
        inputStream.close();

        //System.out.println(code);
        return code;
    }

    /**
     * 解析普通文本文件  流式文件 如txt
     * @param path
     * @return
     */
    @SuppressWarnings("unused")
    public static List<String> readTxt(String path){
        List<String> lines = new ArrayList<>();
        try {
            String code = resolveCode(path);
            File file = new File(path);
            InputStream is = new FileInputStream(file);
            InputStreamReader isr = new InputStreamReader(is, code);
            BufferedReader br = new BufferedReader(isr);
//          char[] buf = new char[1024];
//          int i = br.read(buf);
//          String s= new String(buf);
//          System.out.println(s);
            String str = "";
            while (null != (str = br.readLine())) {
                lines.add(str);
//                System.out.println(str);
            }
            br.close();
        } catch (Exception e) {
            System.err.println("读取文件:" + path + "失败!");
            return null;
        }
        return lines;
    }

    /**
     * 以行为单位读取文件，常用于读面向行的格式化文件
     */
    public static List<String> readFileByLines(String fileName) {
        File file = new File(fileName);
        List<String> lines = new ArrayList<>();
        if(!file.exists())return lines;
        BufferedReader reader = null;
        try {
            //System.out.println("以行为单位读取文件内容，一次读一整行：");
            reader = new BufferedReader(new FileReader(file));
            String tempString = null;
            int line = 1;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                lines.add(tempString);
                //System.out.println("line " + line + ": " + tempString);
                //line++;
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                }
            }
        }
        return lines;
    }

    /**
     * 读取json格式化文件,转化为JSONObject
     */
    public static JSONObject getJson(String fileName){
        JSONObject jsonObject = null;
        StringBuilder json_str = new StringBuilder();
        BufferedReader reader = null;
        try {
            File jsonFile = new File(fileName);
            if (!jsonFile.exists()){
                try {
                    jsonFile.createNewFile();
                    return null;
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            InputStream is = new FileInputStream(jsonFile);
            InputStreamReader isr = new InputStreamReader(is, "UTF-8");
            reader = new BufferedReader(isr);
            String tempString = null;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                json_str.append(tempString);
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            jsonObject = JSONObject.fromObject(json_str.toString());
            try {
                assert reader != null;
                reader.close();
            } catch (IOException e1) {
                System.out.println("关闭文件流时发生了错误！");
            }
        }
        return jsonObject;
    }

    /**
     * 读取json格式化文件,转化为JSONObject
     */
    public static JSONObject readJsonFile(String fileName){
        JSONObject jsonObject = null;
        StringBuilder json_str = new StringBuilder();
        BufferedReader reader = null;
        try {
            File jsonFile = new File(fileName);
            InputStream is = new FileInputStream(jsonFile);
            InputStreamReader isr = new InputStreamReader(is, "UTF-8");
            reader = new BufferedReader(isr);
            String tempString = null;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                json_str.append(tempString);
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            jsonObject = JSONObject.fromObject(json_str.toString());
            try {
                assert reader != null;
                reader.close();
            } catch (IOException e1) {
                System.out.println("关闭文件流时发生了错误！");
            }
        }
        return jsonObject;
    }

    /**
     * 读取json格式化文件,转化为JSONArray
     */
    public static JSONArray getJsonArray(String fileName) {
        JSONArray jsonArray = null;
        StringBuilder json_str = new StringBuilder();
        File jsonFile = new File(fileName);
        if (!jsonFile.exists()){
            try {
                jsonFile.createNewFile();
                return null;
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        BufferedReader reader = null;
        try {
            InputStream is = new FileInputStream(jsonFile);
            InputStreamReader isr = new InputStreamReader(is, "UTF-8");
            reader = new BufferedReader(isr);
            String tempString = null;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                json_str.append(tempString);
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            if (reader != null) {
                jsonArray = JSONArray.fromObject(json_str.toString());
                try {
                    reader.close();
                } catch (IOException e1) {
                    System.out.println("关闭文件流时发生了错误！");
                }
            }
        }
        return jsonArray;
    }

    /**
     * 读取json格式化文件,转化为JSONArray
     */
    public static JSONArray readJsonArrayFile(String fileName) {
        JSONArray jsonArray = null;
        StringBuilder json_str = new StringBuilder();
        File jsonFile = new File(fileName);
        BufferedReader reader = null;
        try {
            InputStream is = new FileInputStream(jsonFile);
            InputStreamReader isr = new InputStreamReader(is, "UTF-8");
            reader = new BufferedReader(isr);
            String tempString = null;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                json_str.append(tempString);
            }
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
            if (reader != null) {
                jsonArray = JSONArray.fromObject(json_str.toString());
                try {
                    reader.close();
                } catch (IOException e1) {
                    System.out.println("关闭文件流时发生了错误！");
                }
            }
        }
        return jsonArray;
    }

    public static void writeFileAll(String fileName, String content){
        try {
            File file =new File(fileName);
            if(!file.exists()){
                boolean fr = file.createNewFile();
                if (!fr)return;
            }
            BufferedWriter writer = null;
            OutputStream os = new FileOutputStream(file);
            OutputStreamWriter osr = new OutputStreamWriter(os, "UTF-8");
            writer = new BufferedWriter(osr);
            writer.write(content);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 显示输入流中还剩的字节数
     */
    private static void showAvailableBytes(InputStream in) {
        int BytesNum = 0;
        try {
            BytesNum = in.available();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
//    public static void main(String[] args){
//        List<String> lines = readTxt("G:\\com.yuanlue.chongwu\\res\\anim\\abc_fade_in.xml");
//        for (String line:lines){
//            System.out.println(line);
//        }
//    }

    /**
     * 压缩文件或路径
     * @param zip 压缩的目的地址
     * @param srcFiles 压缩的源文件
     */
    public static void zipFile( String zip , List<File> srcFiles ){
        try {
            if( zip.endsWith(".zip") || zip.endsWith(".ZIP") ){
                ZipOutputStream _zipOut = new ZipOutputStream(new FileOutputStream(new File(zip))) ;
                _zipOut.setEncoding("GBK");
                for( File _f : srcFiles ){
                    handlerFile(zip , _zipOut , _f , "");
                }
                _zipOut.close();
            }else{
                System.out.println("target file[" + zip + "] is not .zip type file");
            }
        } catch (FileNotFoundException e) {
        } catch (IOException e) {
        }
    }

    /**
     *
     * @param zip 压缩的目的地址
     * @param zipOut
     * @param srcFile  被压缩的文件信息
     * @param path  在zip中的相对路径
     * @throws IOException
     */
    private static void handlerFile(String zip , ZipOutputStream zipOut , File srcFile , String path ) throws IOException{
        System.out.println(" begin to compression file[" + srcFile.getName() + "]");
        if( !"".equals(path) && ! path.endsWith(File.separator)){
            path += File.separator ;
        }
        if( ! srcFile.getPath().equals(zip) ){
            if( srcFile.isDirectory() ){
                File[] _files = srcFile.listFiles() ;
                if( _files.length == 0 ){
                    zipOut.putNextEntry(new ZipEntry( path + srcFile.getName() + File.separator));
                    zipOut.closeEntry();
                }else{
                    for( File _f : _files ){
                        handlerFile( zip ,zipOut , _f , path + srcFile.getName() );
                    }
                }
            }else{
                byte[] _byte = new byte[1024] ;
                InputStream _in = new FileInputStream(srcFile) ;
                zipOut.putNextEntry(new ZipEntry(path + srcFile.getName()));
                int len = 0 ;
                while( (len = _in.read(_byte)) > 0  ){
                    zipOut.write(_byte, 0, len);
                }
                _in.close();
                zipOut.closeEntry();
            }
        }
    }

    /**
     * 解压缩ZIP文件，将ZIP文件里的内容解压到targetDIR目录下
     * @param zipPath 待解压缩的ZIP文件名
     * @param descDir  目标目录
     */
    public static List<File> upzipFile(String zipPath, String descDir) {
        return upzipFile( new File(zipPath) , descDir ) ;
    }

    /**
     * 对.zip文件进行解压缩
     * @param zipFile  解压缩文件
     * @param descDir  压缩的目标地址，如：D:\\测试 或 /mnt/d/测试
     * @return
     */
    @SuppressWarnings("rawtypes")
    public static List<File> upzipFile(File zipFile, String descDir) {
        List<File> _list = new ArrayList<File>() ;
        try {
            ZipFile _zipFile = new ZipFile(zipFile , "GBK") ;
            for( Enumeration entries = _zipFile.getEntries() ; entries.hasMoreElements() ; ){
                ZipEntry entry = (ZipEntry)entries.nextElement() ;
                File _file = new File(descDir + File.separator + entry.getName()) ;
                if( entry.isDirectory() ){
                    _file.mkdirs() ;
                }else{
                    byte[] _byte = new byte[1024] ;
                    File _parent = _file.getParentFile() ;
                    if( !_parent.exists() ){
                        _parent.mkdirs() ;
                    }
                    InputStream _in = _zipFile.getInputStream(entry);
                    OutputStream _out = new FileOutputStream(_file) ;
                    int len = 0 ;
                    while( (len = _in.read(_byte)) > 0){
                        _out.write(_byte, 0, len);
                    }
                    _in.close();
                    _out.flush();
                    _out.close();
                    _list.add(_file) ;
                }
            }
        } catch (IOException e) {
        }
        return _list ;
    }

    /**
     * 对临时生成的文件夹和文件夹下的文件进行删除
     */
    public static void deleteFile(String delpath) {
        try {
            File file = new File(delpath);
            if (!file.isDirectory()) {
                file.delete();
            } else if (file.isDirectory()) {
                String[] filelist = file.list();
                for (int i = 0; i < filelist.length; i++) {
                    File delfile = new File(delpath + File.separator + filelist[i]);
                    if (!delfile.isDirectory()) {
                        delfile.delete();
                    } else if (delfile.isDirectory()) {
                        deleteFile(delpath + File.separator + filelist[i]);
                    }
                }
                file.delete();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void deleteFile(File file){
        if(file.exists()){ //判断文件是否存在
            if(file.isFile()){ //判断是否是文件
                file.delete(); //delete()方法 你应该知道 是删除的意思;
            }else if(file.isDirectory()){ //否则如果它是一个目录
                File files[] = file.listFiles(); //声明目录下所有的文件 files[];
                for(int i=0;i<files.length;i++){ //遍历目录下所有的文件
                    deleteFile(files[i]); //把每个文件 用这个方法进行迭代
                }
            }
            file.delete();
        }else{
            System.out.println("所删除的文件不存在！"+'\n');
        }
    }
    public static void removeFile(String fileName){
        File file = new File(fileName);
        deleteFile(file);
    }

}
