package Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
// 开发者相关
@RequestMapping("/Developer")
public class AboutController {
    // 项目相关
    @RequestMapping("/project")
    public String aboutproject(){
        return "/about/project";
    }
    // 关于我们
    @RequestMapping("/about")
    public String aboutus(){
        return "/about/us";
    }
    // 加入我们
    @RequestMapping("/join")
    public String appendus(){
        return "/about/join";
    }
    // 联系我们
    @RequestMapping("/contact")
    public String callus(){
        return "/about/contact";
    }
}
