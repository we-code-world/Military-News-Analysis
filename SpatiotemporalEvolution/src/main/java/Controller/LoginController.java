package Controller;

import Annotation.AccessLimit;
import Entity.Administrator;
import Entity.User;
import Service.UserInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpSession;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

@Controller
//登录注册相关操作
@RequestMapping("/Login")
public class LoginController {
    @Autowired
    @Qualifier("UserInfoServiceImpl")
    private UserInfoService userInfoService;
    private Administrator admin;
    private User user;

    //用户登录操作
    @AccessLimit(needLogin = false)
    @RequestMapping("/user")
    @ResponseBody
    public Map<String,Object> login_user(HttpSession session,String Account, String password) {
        Map<String,Object> map=new HashMap<String,Object>();
        if(!Pattern.matches("^[a-zA-Z_.@#]{0,}$", password)){
            map.put("result","password_error");
            return map;
        }
        user=userInfoService.findByAccount(Account);
        if(user!=null&&password.equals(user.getPassword())){
            session.setAttribute("userInfo",user);
            map.put("role","user");
            map.put("result","ok");
        }
        else{
            map.put("result","error");
        }
        return map;
    }
    //管理员登录操作
    @AccessLimit(needLogin = false)
    @RequestMapping("/admin")
    @ResponseBody
    public Map<String,Object> login_admin(HttpSession session,String Account, String password) {
        Map<String,Object> map=new HashMap<String,Object>();
        if(!Pattern.matches("^[a-zA-Z_.@#]{0,}$", password)){
            map.put("result","password_error");
            return map;
        }
        admin=userInfoService.findByAccountAdmin(Account);
        if(admin!=null&&password.equals(admin.getPassword())){
            session.setAttribute("admin",admin);
            map.put("role","admin");
            map.put("result","ok");
        }
        else{
            map.put("result","error");
        }
        return map;
    }
    //用户注册操作
    @RequestMapping("/Register")
    @ResponseBody
    public Map<String,Object> register(HttpSession session,String username,String Account,int sex, String password,String Email) {
        Map<String,Object> map=new HashMap<String,Object>();
        if(!Pattern.matches("^[a-zA-Z_.@#]{0,}$", password)){
            map.put("result","password_error");
            return map;
        }
        User user1 = new User();
        user1.setUserName(username);
        user1.setAccount(Account);
        user1.setPassword(password);
        user1.setEmail(Email);
        user1.setSex(sex);
        user1.setPhoto("user2-128x128.jpg");
        user1.setBackground("photo4.png");
        user=userInfoService.findByAccount(Account);
        if(user!=null){
            map.put("result","had");
        }
        else{
            if(userInfoService.setUser(user1)!=0){
                user=userInfoService.findByAccount(Account);
                map.put("result","ok");
                session.setAttribute("userInfo",user);
            }else map.put("result","error");
        }
        return map;
    }
    //用户注册操作
    @RequestMapping("/Register/check/account")
    @ResponseBody
    public Map<String,Object> register_check(String Account) {
        Map<String,Object> map=new HashMap<String,Object>();
        user=userInfoService.findByAccount(Account);
        if(user!=null){
            map.put("result","had");
        }
        else map.put("result","ok");
        return map;
    }
}
