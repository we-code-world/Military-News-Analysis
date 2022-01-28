package Controller;

import Entity.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RequestMapping("/Return")
public class ReturnController {
    @RequestMapping("/request/limit")
    public String OutLimit(){
        return "return/Refresh";
    }
    @RequestMapping("/request/timeout")
    public String SessionTimeOut(){
        return "return/Refresh";
    }
    @RequestMapping("/system/error")
    public String SystemError(){
        return "return/Refresh";
    }
    @RequestMapping("/search/pages")
    public Map<String,Object> PageList(HttpServletRequest request){
        Map<String,Object> map=new HashMap<String,Object>();
        Cookie[] cookies = request.getCookies();
        List<Page> pageList = new ArrayList<>();
        Cookie cookie = new Cookie("describe","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("describe")){
                cookie=ck;
            }
        }
        String describe = cookie.getValue();
        request.getRequestURI().contains("Admin");
        map.put("pages",pageList);
        return map;
    }
}
