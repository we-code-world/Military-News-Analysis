package InterCepter;

import Annotation.AccessLimit;
import Entity.User;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.util.Collections;

public class LimitInterceptor implements HandlerInterceptor{
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        HttpSession session = request.getSession();
        if (handler instanceof HandlerMethod){
            HandlerMethod hm = (HandlerMethod) handler;
            AccessLimit accessLimit = hm.getMethodAnnotation(AccessLimit.class);
            if (accessLimit == null){
                return true;
            }
            int seconds = accessLimit.seconds();
            int maxCount = accessLimit.maxCount();
            boolean login = accessLimit.needLogin();
            User user = (User) session.getAttribute("userInfo");
            if (login && user==null){
                String url = request.getRequestURI().split("/Show")[1];
                int number = url.length()-url.replaceAll("/","").length();
                StringBuilder returnurl = new StringBuilder();
                for (int i=0;i<number;i++) returnurl.append("../");
                request.getRequestDispatcher(returnurl+"Return/limit").forward(request, response);
                return false;
            }
            long now = System.currentTimeMillis();
            if (session.getAttribute("AccessKey") == null ){
                session.setAttribute("AccessKey",1);
                session.setAttribute("CreateTime", now);
                return true;
            }else {
                int count = (int) session.getAttribute("AccessKey");
                long createTime = (long) session.getAttribute("CreateTime");
                if (count < maxCount){
                    if (now - createTime >= seconds*10000){
                        session.setAttribute("AccessKey",1);
                        session.setAttribute("CreateTime", now);
                        return true;
                    }else {
                        session.setAttribute("AccessKey",count+1);
                        return true;
                    }
                }else{
                    session.removeAttribute("AccessKey");
                    session.removeAttribute("CreateTime");
                    String url = request.getRequestURI().split("/Show")[1];
                    int number = url.length()-url.replaceAll("/","").length();
                    StringBuilder returnurl = new StringBuilder();
                    for (int i=0;i<number;i++) returnurl.append("../");
                    request.getRequestDispatcher(returnurl+"Return/limit").forward(request, response);
                    return false;
                }
            }
        }
        return true;
    }
}
