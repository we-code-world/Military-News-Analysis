package InterCepter;

import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.util.Collections;

public class LoginInterceptor implements HandlerInterceptor {
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        HttpSession session = request.getSession();
        if (session.getAttribute("userInfo") != null) {
            return true;
        }else if (request.getRequestURI().contains("/Container")){
            request.getRequestDispatcher("../").forward(request, response);
            return false;
        }else{
            String url = request.getRequestURI().split("/Show")[1];
            int number = url.length()-url.replaceAll("/","").length();
            StringBuilder returnurl = new StringBuilder();
            for (int i=0;i<number;i++) returnurl.append("../");
            request.getRequestDispatcher(returnurl+"Return/timeout").forward(request, response);
            return false;
        }
    }
}