package Tools;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PyRunner {
    private String PyPath;
    private String python;
    public PyRunner(){
        PyPath="C:/Users/ASUS/Desktop";
    }
    public PyRunner(String path){
        PyPath=path;
        if (PyPath.contains(":"))python = "python";
        else python = "python3";
    }
    public boolean RunPy(String pyName, List<String> params){
        Process proc;
        Boolean sign =true;
        try {
            proc = Runtime.getRuntime().exec(python +" "+PyPath+"/"+pyName+".py");// 执行py文件
            //用输入输出流来截取结果
            OutputStream out = proc.getOutputStream();
            for (String param:params) {
                out.write(param.getBytes());
                out.write("\n".getBytes());
            }
            out.close();
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            BufferedReader err = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String line = null;
            while ((line = in.readLine())!=null) {
                System.out.println(line);
            }
            while ((line = err.readLine())!=null) {
                System.out.println(line);
                sign = false;
            }
            in.close();
            err.close();
            //out.write(111);
            //out.close();
            /*in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            err = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            while ((line = in.readLine())!=null) {
                System.out.println(line);
            }
            while ((line = err.readLine())!=null) {
                System.out.println(line);
            }
            //out.write(111);
            in.close();
            err.close();*/
            proc.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
        return sign;
    }
    public List<String> RunPyResult(String pyName, List<String> params){
        Process proc;
        List<String> result_lines = new ArrayList<>();
        try {
            proc = Runtime.getRuntime().exec(python + " "+PyPath+"/"+pyName+".py");// 执行py文件
            //用输入输出流来截取结果
            OutputStream out =proc.getOutputStream();
            for (String param:params) {
                out.write(param.getBytes());
                out.write("\n".getBytes());
            }
            out.close();
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            BufferedReader err = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String line = null;
            while ((line = in.readLine())!=null) {
                System.out.println(line);
                if(!line.equals(""))result_lines.add(line);
            }
            while ((line = err.readLine())!=null) {
                System.out.println(line);
            }
            in.close();
            err.close();
            proc.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
            return result_lines;
        }
        return result_lines;
    }

    public List<String> getLineFromMarkTXT(String fileName){
        List<String> rtn_lines = new ArrayList<>();
        Process proc;
        try {
            proc = Runtime.getRuntime().exec(python+" "+PyPath+"/utils/file/read.py");// 执行py文件
            //用输入输出流来截取结果
            OutputStream out =proc.getOutputStream();
            List<String> params = new ArrayList<>(Arrays.asList("readNews2Seq", fileName));
            for (String param:params) {
                out.write(param.getBytes());
                out.write("\n".getBytes());
            }
            out.close();
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            BufferedReader err = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String line = null;
            while ((line = in.readLine())!=null) {
                if(!line.equals(""))rtn_lines.add(line);
            }
            while ((line = err.readLine())!=null) {
                System.out.println(line);
            }
            in.close();
            err.close();
            proc.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
        return rtn_lines;
    }
    public void createLineFromMarkTXT(String fileName,String outfile){
        Process proc;
        try {
            proc = Runtime.getRuntime().exec(python+" "+PyPath+"/utils/file/read.py");// 执行py文件
            //用输入输出流来截取结果
            OutputStream out =proc.getOutputStream();
            List<String> params = new ArrayList<>(Arrays.asList("createNews2Seq", fileName, outfile));
            for (String param:params) {
                out.write(param.getBytes());
                out.write("\n".getBytes());
            }
            out.close();
            BufferedReader err = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String line = null;
            while ((line = err.readLine())!=null) {
                System.out.println(line);
            }
            err.close();
            proc.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
//    public static void main(String[] args){
//        List<String> myParams;
//        myParams = new ArrayList<>();
//        myParams.add("2021");
//        String pyname = "url_scrapper";
//        myParams.add("100");
//        myParams.add("20");
//        new PyRunner(new Container().PyPath).RunPyResult(pyname,myParams);
//        System.out.println("run out");
//    }
}
