package Controller;

import Service.WeaponService;
import Tools.Container;
import net.sf.json.JSONObject;
import org.apache.commons.lang.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@Controller
@RequestMapping("/Resource")
public class ResourceController {
    @Autowired
    @Qualifier("WeaponServiceImpl")
    private WeaponService weaponService;
    public Container container = new Container();
    String basePath=container.ResPath + "/";
    String[] file_list= new File(basePath).list();
    @RequestMapping("/download/{file}")
    @ResponseBody
    public void downloadJSON(HttpServletResponse response, HttpServletRequest request,@PathVariable(value = "file",required = true) String fileName) throws IOException {
        response.setContentType("application/force-download;charset=UTF-8");
        final String userAgent = request.getHeader("USER-AGENT");
        try {
            if (StringUtils.contains(userAgent, "MSIE") || StringUtils.contains(userAgent, "Edge")) {// IE浏览器
                fileName = URLEncoder.encode(fileName, "UTF8");
            } else if (StringUtils.contains(userAgent, "Mozilla")) {// google,火狐浏览器
                fileName = new String(fileName.getBytes(), "ISO8859-1");
            } else {
                fileName = URLEncoder.encode(fileName, "UTF8");// 其他浏览器
            }
            response.setHeader("Content-disposition", "attachment; filename=" + fileName);
        } catch (UnsupportedEncodingException e) {
            System.out.println(e.getMessage());
        }
        InputStream in = null;
        OutputStream out = null;
        try {
            //获取要下载的文件输入流
            in = new FileInputStream(basePath+fileName);
            int len = 0;
            //创建数据缓冲区
            byte[] buffer = new byte[1024];
            //通过response对象获取outputStream流
            out = response.getOutputStream();
            //将FileInputStream流写入到buffer缓冲区
            while((len = in.read(buffer)) > 0) {
                //使用OutputStream将缓冲区的数据输出到浏览器
                out.write(buffer,0,len);
            }
            //这一步走完，将文件传入OutputStream中后，页面就会弹出下载框
        } catch (Exception e) {
            e.printStackTrace();
            try {
                response.sendError(404, "File not found!");
            } catch (IOException e1) {
                e1.printStackTrace();
            }
        } finally {
            try {
                if (out != null)
                    out.close();
                if(in!=null)
                    in.close();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    @RequestMapping("/upload")
    @ResponseBody
    public JSONObject upload_file(@RequestParam(value = "file") MultipartFile file,
                                  @RequestParam(value = "change", required = false, defaultValue = "0") int sign,
                                  @RequestParam(value = "type", required = false, defaultValue = "") String save) {
        Map<String,Object> map=new HashMap<String,Object>();
        if (!file.isEmpty()) {
            String originalFilename = file.getOriginalFilename();
            long size = file.getSize();
            System.out.println("上传文件名为" + originalFilename + ",上传大小为" + size);
            // 设置保存路径
            String filenames = originalFilename;
            String url="";
            if (sign==1){
                String uuid = UUID.randomUUID().toString();
                // 获取后缀名
                assert originalFilename != null;
                int lastIndexOf = originalFilename.lastIndexOf(".");
                String substring = originalFilename.substring(lastIndexOf);
                filenames = uuid + substring;
                url = uuid+substring;
            }
            if(save.equals("")){
                filenames = container.ResPath + filenames;
            }else{
                filenames = container.ServletPath + save + filenames;
                url = save + url;
                map.put("url",url);
            }
            File files = new File(filenames);
            try {
                //以绝对路径保存重名命后的文件
                file.transferTo(files);
                map.put("result","ok");
            } catch (IllegalStateException e) {
                map.put("result","error");
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
                map.put("result","error");
            }
        }
        return JSONObject.fromObject(map);
    }
    @RequestMapping("/map")
    public void getPosition(){
        String url= "http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak="+container.baiduMapAK;
    }
    //获取武器装备列表
    @RequestMapping("/weapon/list")
    public String getWeaponList(){
        return "";
    }
}
