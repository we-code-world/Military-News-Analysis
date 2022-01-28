package Controller;

import Entity.*;
import Service.*;
import Tools.Container;
import Tools.DateUtils;
import Tools.FileIO;
import Tools.PyRunner;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import org.apache.commons.lang.StringUtils;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.*;
import java.net.URLEncoder;
import java.util.*;

@Controller
@RequestMapping("/Admin")
//后台管理相关操作
public class BackstageController {
    @Autowired
    @Qualifier("UserInfoServiceImpl")
    UserInfoService userInfoService;
    @Autowired
    @Qualifier("NewsServiceImpl")
    private NewsService newsService;
    @Autowired
    @Qualifier("LocationServiceImpl")
    private LocationService locationService;
    @Autowired
    @Qualifier("WeaponServiceImpl")
    private WeaponService weaponService;
    @Autowired
    @Qualifier("EventServiceImpl")
    private EventService eventService;
    public Container container = new Container();
    PyRunner myRunner = new PyRunner(container.PyPath);
    String basePath=container.DataPath + "/mark/txt/";
    String[] file_list= new File(basePath).list();
    List<Integer> file_num_list = new ArrayList<>();
    @RequestMapping("/show")
    public String AfterLogin(Model model, HttpSession session){
        Administrator admin = (Administrator) session.getAttribute("admin");
        model.addAttribute("admin_name",admin.getUserName());
        return "backstage/back_page";
    }
    @RequestMapping("/detail")
    public String ShowDetail(Model model, HttpSession session){
        Administrator admin = (Administrator) session.getAttribute("admin");
        model.addAttribute("admin_name",admin.getUserName());
        return "backstage/back_page";
    }
    @RequestMapping("/logout")
    public String Logout(HttpSession session){
        session.removeAttribute("admin");
        return "redirect:/";
    }
    @RequestMapping("/general/change")
    public String changeCenter(Model model, HttpSession session){
        return "backstage/general/home/change_page";
    }
    @RequestMapping("/general/center")
    public String showCenter(Model model, HttpSession session){
        return "backstage/general/home/home_page";
    }
    @RequestMapping("/general/users")
    public String usersCenter(Model model, HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie = new Cookie("pageNum","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageNum")){
                cookie=ck;
            }
        }
        String pageNum = cookie.getValue();
        int num = pageNum.equals("") ? 1 : Integer.parseInt(pageNum);
        PageInfo<User> users= userInfoService.pageAll(num,15);
        List<User> usersList = users.getList();
        List<UserInfo> userInfoList = new ArrayList<>();
        for (User u: usersList){
            UserInfo U = new UserInfo(u);
            userInfoList.add(U);
        }
        model.addAttribute("pageDetil",users);
        model.addAttribute("user_list",userInfoList);
        return "backstage/general/manage/users_page";
    }
    @RequestMapping("/general/crawler")
    public String crawlerCenter(){ return "backstage/general/manage/crawler_run"; }
    @RequestMapping("/general/crawler/start")
    @ResponseBody
    public Map<String,Object> startCrawler(@Param("sign") int sign,@Param("pyNum") int pyNum,@Param("offset") int offset,@Param("time1") String time1,@Param("time2") String time2){
        Map<String,Object> map=new HashMap<String,Object>();
        String pyname = "test";
        List<String> myParams;
        Boolean run_result = true;
        try{
            if (sign==1){
                List<String> years = DateUtils.getYearList(time1,time2);
                for (String yearStr:years) {
                    myParams = new ArrayList<>();
                    myParams.add(container.RootPath);
                    myParams.add(yearStr);
                    if (pyNum == 1){
                        pyname = "url_scrapper";
                        myParams.add(""+offset);
                        myParams.add("20");
                        List<String> lines = myRunner.RunPyResult(pyname,myParams);
                        map.put("IF_RUN",1);
                        map.put("OFFSET",offset+20);
                        System.out.println(offset);
                        for(String line : lines){
                            if (line.equals("error")) run_result = false;
                            if (line.equals("end")){
                                map.put("IF_RUN",1);
                                map.put("Content",line);
                            }
                            if (line.equals("end")){
                                map.put("IF_RUN",0);
                            }
                        }
                    }
                    else if (pyNum == 2){
                        pyname = "article_scrapper";
                        run_result = myRunner.RunPy(pyname,myParams);
                        map.put("IF_RUN",0);
                    }
                }
                if (!run_result) {
                    map.put("result","error");
                    map.put("IF_RUN",0);
                    return map;
                }
                map.put("result","ok");
            }
            else map.put("result","error");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","error");
        }
        return map;
    }
    //数据源返回新闻列表
    @RequestMapping("/general/news")
    public String Newscenter(Model model, HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_num = new Cookie("pageNum","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageNum")){
                cookie_num=ck;
            }
        }
        String pageNum = cookie_num.getValue();
        int num = pageNum.equals("") ? 1 : Integer.parseInt(pageNum);
        PageInfo<News> pageNews = newsService.pageAll(num,15);
        model.addAttribute("pageDetil",pageNews);
        return "backstage/general/manage/news_source";
    }
    //新闻详细内容
    @RequestMapping("/general/news/Detail")
    public String NewsDetail(Model model, HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("pageID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        int ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        News ns = newsService.findByID(ID);
        model.addAttribute("news",ns);
        List<String> article_lines = new ArrayList<>();
        try {
            List<String> lines= FileIO.readTxt(container.DataPath+ns.getNewsPos() + ".txt");
            for (int i = 4; i<lines.size();i++){
                String line = lines.get(i);
                if (line.replaceAll(" ","").equals(""))continue;
                article_lines.add(line);
            }
            model.addAttribute("article_lines",article_lines);
        }catch (Exception e){
            e.printStackTrace();
            return "forward:/Return/system/error";
        }
        return "backstage/general/manage/news/news_detail";
    }
    @RequestMapping("/general/events")
    public String database(){
        return "backstage/general/manage/event_result";
    }
    @RequestMapping("/general/event/list")
    public String database_detail(Model model, HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_num = new Cookie("pageNum","");
        Cookie cookie_name = new Cookie("databaseName","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageNum")){
                cookie_num=ck;
            }else if (ck.getName().equals("databaseName")){
                cookie_name=ck;
            }
        }
        String pageNum = cookie_num.getValue();
        String dbName = cookie_name.getValue();
        int num = pageNum.equals("") ? 1 : Integer.parseInt(pageNum);
        switch (dbName) {
            case "accident":
                PageInfo<Event> pageAcc = eventService.pageAllAccidentEvent(num,15);
                model.addAttribute("pageDetil",pageAcc);
                return "backstage/general/manage/events_db/database_accident_event";
            case "conflict":
                PageInfo<EventBrief> pageCon = eventService.pageAllConflictEvent(num,15);
                model.addAttribute("pageDetil",pageCon);
                return "backstage/general/manage/events_db/database_conflict_event";
            case "key_sentence":
                PageInfo<KeySentence> pageKey = weaponService.pageAllKeySentences(num,15);
                model.addAttribute("pageDetil",pageKey);
                return "backstage/general/manage/events_db/database_keysentence";
            case "locationPage":
                PageInfo<Location> pageLoc = locationService.pageAll(num,15);
                model.addAttribute("pageDetil",pageLoc);
                return "backstage/general/manage/events_db/database_location";
            case "practice":
                PageInfo<PracticeEvent> pagePra = eventService.pageAllPracticeEvent(num,15);
                model.addAttribute("pageDetil",pagePra);
                return "backstage/general/manage/events_db/database_practice_event";
            case "provocative":
                PageInfo<ProvocativeEvent> pagePro = eventService.pageAllProvocativeEvent(num,15);
                model.addAttribute("pageDetil",pagePro);
                return "backstage/general/manage/events_db/database_provocative_event";
            case "rd":
                PageInfo<RDEvent> pageRD = eventService.pageAllRDEvent(num,15);
                model.addAttribute("pageDetil",pageRD);
                return "backstage/general/manage/events_db/database_rd_event";
            case "transaction":
                PageInfo<TransactionEvent> pageTra = eventService.pageAllTransactionEvent(num,15);
                model.addAttribute("pageDetil",pageTra);
                return "backstage/general/manage/events_db/database_transaction_event";
            case "weapon":
                PageInfo<Weapon> pageWea = weaponService.pageAllWeapons(num,15);
                model.addAttribute("pageDetil",pageWea);
                return "backstage/general/manage/events_db/database_weapon";
            default:
                return "forward:/Return/system/error";
        }
    }
    //事件抽取结果
    @RequestMapping("/general/Events/Detail")
    public String EventsDetail(Model model, HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("eventID","");
        Cookie cookie_Class = new Cookie("databaseName","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("eventID")){
                cookie_ID=ck;
            }else if (ck.getName().equals("databaseName")){
                cookie_Class=ck;
            }
        }
        String eventID = cookie_ID.getValue();
        String eventClass = cookie_Class.getValue();
        int ID = eventID.equals("") ? 1 : Integer.parseInt(eventID);
        int newsID = 1;
        String sentencesID ="";
        switch (eventClass) {
            case "accident":
                AccidentEvent Acc = eventService.getAccidentEventByID(ID);
                sentencesID = Acc.getSentenceID();
                break;
            //newsID = Acc.getSentenceID();
            case "conflict":
                EventBrief Con = eventService.getConflictEventByID(ID);
                sentencesID = Con.getSentenceID();
                break;
            case "practice":
                PracticeEvent Pra = eventService.getPracticeEventByID(ID);
                sentencesID = Pra.getSentenceID();
                break;
            case "provocative":
                ProvocativeEvent Pro = eventService.getProvocativeEventByID(ID);
                sentencesID = Pro.getSentenceID();
                break;
            case "rd":
                RDEvent RD = eventService.getRDEventByID(ID);
                sentencesID = RD.getSentenceID();
                break;
            case "transaction":
                TransactionEvent Tra = eventService.getTransactionEventByID(ID);
                sentencesID = Tra.getSentenceID();
                break;
            default:
                return "forward:/Return/system/error";
        }
        newsID = weaponService.getSentenceByID(Integer.parseInt(sentencesID.split(";")[0])).getNewsID();
        News ns = newsService.findByID(newsID);
        model.addAttribute("news",ns);
        List<String> article_lines = new ArrayList<>();
        try {
            List<String> lines= FileIO.readTxt(container.DataPath+ns.getNewsPos() + ".txt");
            int j = 0;
            for (int i = 4; i<lines.size();i++){
                String line = lines.get(i);
                if (line.replaceAll(" ","").equals(""))continue;
                String line_s = line.replaceAll("[！？!?。]","").replaceAll("······","·····");
                int num_sen = line.length()-line_s.length();
                for(int line_j = 0;line_j<num_sen;line_j++){
                    j++;
                    KeySentence ks = weaponService.getAllKeySentencesByNewsIDAndNum(newsID,j);
                    if (ks == null){
                        continue;
                    }
                    if (ks.getMatchTime()!=null)
                        for (String item:ks.getMatchTime().split(";")){
                            line = line.replace(item,"<span class=\"hljs-quote\">"+item+"</span>");
                        }
                    if (ks.getMatchLoc()!=null)
                        for (String item:ks.getMatchLoc().split(";")){
                            line = line.replace(item,"<span class=\"hljs-name\">"+item+"</span>");
                        }
                    if (ks.getWeaponName()!=null)
                        for (String item:ks.getWeaponName().split(";")){
                            line = line.replace(item,"<span class=\"hljs-attr\">"+item+"</span>");
                        }
                    if (ks.getEventTrigger()!=null)
                        for (String item:ks.getEventTrigger().split(";")){
                            line = line.replace(item,"<span class=\"hljs-meta\">"+item+"</span>");
                        }
                }
                article_lines.add(line);
            }
            model.addAttribute("article_lines",article_lines);
        }catch (Exception e){
            e.printStackTrace();
            return "forward:/Return/system/error";
        }
        List<KeySentence> kss = weaponService.getAllKeySentencesByNewsID(newsID);
        List<String> timeList = new ArrayList<>();
        List<String> locList = new ArrayList<>();
        List<String> weaponList = new ArrayList<>();
        List<String> triggerList = new ArrayList<>();
        for (KeySentence ks : kss ){
            if (ks.getMatchTime()!=null)
                timeList.addAll(Arrays.asList(ks.getMatchTime().split(";")));
            if (ks.getMatchLoc()!=null)
                locList.addAll(Arrays.asList(ks.getMatchLoc().split(";")));
            if (ks.getWeaponName()!=null)
                weaponList.addAll(Arrays.asList(ks.getWeaponName().split(";")));
            if (ks.getEventTrigger()!=null)
                triggerList.addAll(Arrays.asList(ks.getEventTrigger().split(";")));
        }
        model.addAttribute("timeList",timeList);
        model.addAttribute("locList",locList);
        model.addAttribute("weaponList",weaponList);
        model.addAttribute("triggerList",triggerList);
        return "backstage/general/manage/news/result_detail";
    }
    //提交未抽取出信息
    @RequestMapping("/general/events/Detail/submit")
    @ResponseBody
    public Map<String,Object> getNewsDetailSubmit(HttpSession session, HttpServletRequest request,String tag,int catelogid){
        Map<String,Object> map=new HashMap<String,Object>();
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("pageID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        int ID = cookie_ID.getValue().equals("")? 1: Integer.parseInt(pageID);
        User user = (User) session.getAttribute("userInfo");
        if(tag != null){
            map.put("result","ok");
        }else map.put("result","error");
        return map;
    }
    @RequestMapping("/general/human")
    public String humanNews(Model model, HttpServletRequest request, HttpServletResponse response){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("markID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("markID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        this.file_num_list = new ArrayList<>();
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            file_num_list.add(Integer.parseInt(file_name[file_name.length - 1]));
        }
        Collections.sort(file_num_list);
        int news_ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        int ID = 0;
        try{
            ID = file_num_list.get(news_ID - 1);
        }catch (IndexOutOfBoundsException e){
            ID = file_num_list.get(0);
            Cookie cookie = new Cookie("markID","1"); // 新建Cookie
            cookie.setMaxAge(60*60); // 设置生命周期为60*60
            response.addCookie(cookie); // 输出到客户端
        }

        JSONArray article_lines = new JSONArray();
        try {
            List<String> lines= FileIO.readTxt(container.DataPath + "/mark/txt/" + ID + ".txt");
            if (lines == null){
                lines= FileIO.readTxt(container.DataPath + "/mark/txt/" + file_num_list.get(0) + ".txt");
                ID = file_num_list.get(0);
                Cookie cookie = new Cookie("markID","1"); // 新建Cookie
                cookie.setMaxAge(60*60); // 设置生命周期为60*60
                response.addCookie(cookie); // 输出到客户端
            }
            assert lines != null;
            myRunner.createLineFromMarkTXT(container.DataPath + "/mark/txt/" + ID + ".txt",container.DataPath + "/mark/txt_lines/" + ID + ".txt");
            List<String> div_lines = FileIO.readTxt(container.DataPath + "/mark/txt_lines/" + ID + ".txt");
            int check_id = Integer.parseInt(div_lines.get(0));
            JSONArray jsonArray = null;
            if (!new File(container.DataPath + "/mark/json/" + ID + ".json").exists()){
                jsonArray = new JSONArray();
                JSONObject jsonObject = null;
                String line = null;
                for (int i = 1; i<div_lines.size();i++){
                    line = div_lines.get(i);
                    jsonObject = new JSONObject();
                    jsonObject.put("sentence",line);
                    JSONArray newJsonArr = new JSONArray();
                    JSONObject arguments = new JSONObject();
                    arguments.put("time",newJsonArr);
                    arguments.put("loc",newJsonArr);
                    arguments.put("weapon",newJsonArr);
                    arguments.put("country",newJsonArr);
                    JSONArray events = new JSONArray();
                    jsonObject.put("arguments",arguments);
                    jsonObject.put("events",events);
                    jsonArray.add(jsonObject);
                }
                FileIO.writeFileAll(container.DataPath + "/mark/json/" + ID + ".json",jsonArray.toString());
                //FileIO.writeFileAll(container.DataPath + "/mark/json/" + ID + ".json","jsonArray.toString()");
            }else jsonArray = FileIO.readJsonArrayFile(container.DataPath + "/mark/json/" + ID + ".json");
            if (lines.size()>4){
                model.addAttribute("url",lines.get(0));
                model.addAttribute("newsSource",lines.get(2).replaceAll("来源：",""));
                model.addAttribute("Date",lines.get(3));
                JSONObject ont_line = null;
                JSONArray lines_items = null;
                JSONArray rtn_times = new JSONArray();
                JSONArray rtn_locs = new JSONArray();
                JSONArray rtn_countrys = new JSONArray();
                JSONArray rtn_weapons = new JSONArray();
                JSONArray rtn_triggers = new JSONArray();
                JSONArray seqs_items = new JSONArray();
                JSONObject seqs_item = null;
                String seqs = "";
                for (int arr_id=0;arr_id<jsonArray.size();arr_id++){
                    seqs_item = new JSONObject();
                    JSONObject thisLine = jsonArray.getJSONObject(arr_id);
                    seqs = thisLine.getString("sentence");
                    JSONObject arguements = thisLine.getJSONObject("arguments");
                    JSONArray events = thisLine.getJSONArray("events");
                    JSONArray Times = arguements.getJSONArray("time");
                    JSONArray Locs = arguements.getJSONArray("loc");
                    JSONArray Countrys = arguements.getJSONArray("country");
                    JSONArray Weapons = arguements.getJSONArray("weapon");
                    seqs_item.put("source",seqs);
                    String rtn_seqs = "";
                    int start_id = 0;
                    int end_id = 0;
                    List<String> mark_points = new ArrayList<>();
                    char[] seq2chars = seqs.toCharArray();
                    mark_points.add("0");
                    for (char s:seq2chars)mark_points.add("0");
                    for (Object item:events){
                        JSONObject event = (JSONObject)item;
                        String trigger = event.getJSONObject("trigger").getString("text");
                        String subject = event.getJSONObject("subject").getString("text");
                        String object = event.getJSONObject("object").getString("text");
                        rtn_triggers.add("【"+subject+"】"+trigger+"【"+object+"】");
                        if (!subject.equals("")) {
                            start_id = event.getJSONObject("subject").getInt("offset");
                            end_id = start_id + event.getJSONObject("subject").getInt("length");
                            mark_points.set(start_id,mark_points.get(start_id)+"-2");
                            mark_points.set(end_id,mark_points.get(end_id)+"-1");
                            //seqs = seqs.replace(subject, "<span style=\"background:#337ab7\">" + subject + "</span>");
                        }
                        if (!object.equals("")) {
                            start_id = event.getJSONObject("object").getInt("offset");
                            end_id = start_id + event.getJSONObject("object").getInt("length");
                            mark_points.set(start_id,mark_points.get(start_id)+"-3");
                            mark_points.set(end_id,mark_points.get(end_id)+"-1");
                            //seqs = seqs.replace(object, "<span style=\"background:#5bc0de\">" + object + "</span>");
                        }
                        if (!trigger.equals("")) {
                            start_id = event.getJSONObject("trigger").getInt("offset");
                            end_id = start_id + event.getJSONObject("trigger").getInt("length");
                            mark_points.set(start_id,mark_points.get(start_id)+"-4");
                            mark_points.set(end_id,mark_points.get(end_id)+"-1");
                            //seqs = seqs.replace(trigger,"<span style=\"color:#d9534f\">"+trigger+"</span>");
                        }
                    }
                    for (Object item:Times){
                        String time = ((JSONObject)item).getString("text");
                        rtn_times.add(time);
                        start_id = ((JSONObject)item).getInt("offset");
                        end_id = start_id + ((JSONObject)item).getInt("length");
                        mark_points.set(start_id,mark_points.get(start_id)+"-5");
                        mark_points.set(end_id,mark_points.get(end_id)+"-1");
                        //seqs = seqs.replace(time,"<span style=\"color:#5cb85c\">"+time+"</span>");
                    }
                    for (Object item:Locs){
                        String loc = ((JSONObject)item).getString("text");
                        rtn_locs.add(loc);
                        start_id = ((JSONObject)item).getInt("offset");
                        end_id = start_id + ((JSONObject)item).getInt("length");
                        mark_points.set(start_id,mark_points.get(start_id)+"-6");
                        mark_points.set(end_id,mark_points.get(end_id)+"-1");
                        //seqs = seqs.replace(loc,"<span style=\"color:#5cb85c\">"+loc+"</span>");
                    }
                    for (Object item:Countrys){
                        String country = ((JSONObject)item).getString("text");
                        rtn_countrys.add(country);
                        start_id = ((JSONObject)item).getInt("offset");
                        end_id = start_id + ((JSONObject)item).getInt("length");
                        mark_points.set(start_id,mark_points.get(start_id)+"-7");
                        mark_points.set(end_id,mark_points.get(end_id)+"-1");
                        //seqs = seqs.replace(country,"<span style=\"color:#337ab7\">"+country+"</span>");
                    }
                    for (Object item:Weapons){
                        String weapon = ((JSONObject)item).getString("text");
                        rtn_weapons.add(weapon);
                        start_id = ((JSONObject)item).getInt("offset");
                        end_id = start_id + ((JSONObject)item).getInt("length");
                        mark_points.set(start_id,mark_points.get(start_id)+"-8");
                        mark_points.set(end_id,mark_points.get(end_id)+"-1");
                        //seqs = seqs.replace(weapon,"<span style=\"color:#5bc0de\">"+weapon+"</span>");
                    }
                    for (int char_i = 0;char_i<seqs.length();char_i++){
                        if (!mark_points.get(char_i).equals("0")){
                            String[] modes = mark_points.get(char_i).split("-");
                            Arrays.sort(modes);
                            for (String mode:modes){
                                switch (mode){
                                    case "0":
                                        break;
                                    case "1":
                                        rtn_seqs+="</span>";
                                        break;
                                    case "2":
                                        rtn_seqs+="<span style=\"background:#337ab7\">";
                                        break;
                                    case "3":
                                        rtn_seqs+="<span style=\"background:#5bc0de\">";
                                        break;
                                    case "4":
                                        rtn_seqs+="<span style=\"color:#d9534f\">";
                                        break;
                                    case "5":
                                        rtn_seqs+="<span style=\"color:#5cb85c\">";
                                        break;
                                    case "6":
                                        rtn_seqs+="<span style=\"color:#5cb85c\">";
                                        break;
                                    case "7":
                                        rtn_seqs+="<span style=\"color:#337ab7\">";
                                        break;
                                    case "8":
                                        rtn_seqs+="<span style=\"color:#5bc0de\">";
                                        break;
                                    default:
                                        break;
                                }
                            }
                        }
                        rtn_seqs+=seq2chars[char_i];
                    }
                    seqs_item.put("seq",rtn_seqs);
                    seqs_item.put("lineID",arr_id);
                    seqs_items.add(seqs_item);
                }
                String rtn_tittle = "";
                JSONArray tittles = new JSONArray();
                JSONObject myTittle = null;
                for (int tittle_id=0;tittle_id<check_id;tittle_id++){
                    myTittle = new JSONObject();
                    JSONObject TEMP = seqs_items.getJSONObject(tittle_id);
                    rtn_tittle = TEMP.getString("seq");
//                    rtn_tittle = rtn_tittle.replaceAll("class=\"hljs-quote\"","style=\"color:#5cb85c\"");
//                    rtn_tittle = rtn_tittle.replaceAll("class=\"hljs-name\"","style=\"color:#337ab7\"");
//                    rtn_tittle = rtn_tittle.replaceAll("class=\"hljs-meta\"","style=\"color:#5bc0de\"");
//                    rtn_tittle = rtn_tittle.replaceAll("class=\"hljs-attr\"","style=\"color:#d9534f\"");
                    myTittle.put("seq",rtn_tittle);
                    myTittle.put("lineID",TEMP.getInt("lineID"));
                    myTittle.put("source",TEMP.getString("source"));
                    tittles.add(myTittle);
                }
                model.addAttribute("newsTittle",tittles);
                for (int i = 4; i<lines.size();i++){
                    ont_line = new JSONObject();
                    lines_items = new JSONArray();
                    String line = lines.get(i);
                    if (line.replaceAll(" ","").equals(""))continue;
                    while (check_id<jsonArray.size()){
                        JSONObject thisLine = jsonArray.getJSONObject(check_id);
                        if (line.contains(thisLine.getString("sentence"))){
                            lines_items.add(seqs_items.get(check_id));
                            check_id ++;
                        }else break;
                    }
                    ont_line.put("seqs",lines_items);
                    article_lines.add(ont_line);
                }
                model.addAttribute("timeList",rtn_times);
                model.addAttribute("locList",rtn_locs);
                model.addAttribute("countryList",rtn_countrys);
                model.addAttribute("weaponList",rtn_weapons);
                model.addAttribute("triggerList",rtn_triggers);
            }
            model.addAttribute("article_lines",article_lines);
            model.addAttribute("NewsID",news_ID);
        }catch (Exception e){
            e.printStackTrace();
        }
        return "backstage/general/manage/news/news_mark";
    }
    //提交未抽取出信息
    @RequestMapping("/general/human/mark/delete")
    @ResponseBody
    public Map<String,Object> deleteSubmit(HttpSession session, HttpServletRequest request,String lineID,String textOffset){
        Map<String,Object> map=new HashMap<String,Object>();
        JSONArray rtn_list = new JSONArray();
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("markID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("markID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        String basePath=container.DataPath + "/mark/txt/";
        file_num_list = new ArrayList<>();
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            file_num_list.add(Integer.parseInt(file_name[file_name.length - 1]));
        }
        int news_ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        int ID = file_num_list.get(news_ID - 1);
        if(textOffset != null && !textOffset.equals("") && lineID != null && !lineID.equals("")){
            int offset = Integer.parseInt(textOffset);
            int lineNum = Integer.parseInt(lineID);
            JSONArray jsonArray = FileIO.readJsonArrayFile(container.DataPath + "/mark/json/"+ID+".json");
            assert jsonArray != null;
            for (int seq_i=0;seq_i<lineNum;seq_i++)rtn_list.add(jsonArray.get(seq_i));
            JSONObject changeTo = new JSONObject();
            JSONObject jsonObject = (JSONObject) jsonArray.get(lineNum);
            assert jsonObject != null;
            changeTo.put("sentence",jsonObject.get("sentence"));
            JSONObject arguments = jsonObject.getJSONObject("arguments");
            JSONArray events = jsonObject.getJSONArray("events");
            JSONObject args = new JSONObject();
            JSONArray newEvents = new JSONArray();
            JSONArray newTimes = new JSONArray();
            for (Object role:arguments.getJSONArray("time")){
                int role_offset = ((JSONObject)role).getInt("offset");
                int role_length = ((JSONObject)role).getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newTimes.add(role);
            }
            JSONArray newLocs = new JSONArray();
            for (Object role:arguments.getJSONArray("loc")){
                int role_offset = ((JSONObject)role).getInt("offset");
                int role_length = ((JSONObject)role).getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newLocs.add(role);
            }
            JSONArray newWeapons = new JSONArray();
            for (Object role:arguments.getJSONArray("weapon")){
                int role_offset = ((JSONObject)role).getInt("offset");
                int role_length = ((JSONObject)role).getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newWeapons.add(role);
            }
            JSONArray newCountrys = new JSONArray();
            for (Object role:arguments.getJSONArray("country")){
                int role_offset = ((JSONObject)role).getInt("offset");
                int role_length = ((JSONObject)role).getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newCountrys.add(role);
            }
            args.put("time",newTimes);
            args.put("loc",newLocs);
            args.put("country",newCountrys);
            args.put("weapon",newWeapons);
            changeTo.put("arguments",args);
            JSONObject empty = new JSONObject();;
            empty.put("text","");
            empty.put("offset",0);
            empty.put("length",0);
            for(Object event:events){
                JSONObject newEvent = new JSONObject();
                JSONObject role = ((JSONObject)event).getJSONObject("trigger");
                int role_offset = role.getInt("offset");
                int role_length = role.getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newEvent.put("trigger",role);
                else continue;
                role = ((JSONObject)event).getJSONObject("subject");
                role_offset = role.getInt("offset");
                role_length = role.getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newEvent.put("subject",role);
                else newEvent.put("subject",empty);
                role = ((JSONObject)event).getJSONObject("object");
                role_offset = role.getInt("offset");
                role_length = role.getInt("length");
                if (!(role_offset <= offset && offset <= role_offset + role_length))
                    newEvent.put("object",role);
                else newEvent.put("object",empty);
                newEvents.add(newEvent);
            }
            changeTo.put("events",newEvents);
            rtn_list.add(changeTo);
            for (int seq_i=lineNum+1;seq_i<jsonArray.size();seq_i++)rtn_list.add(jsonArray.get(seq_i));
            FileIO.writeFileAll(container.DataPath + "/mark/json/"+ID+".json",rtn_list.toString());
            map.put("result","ok");
        }else map.put("result","error");
        return map;
    }
    //提交未抽取出信息
    @RequestMapping("/general/human/submit")
    @ResponseBody
    public Map<String,Object> markNewsSubmit(HttpSession session, HttpServletRequest request,String tag,String catelogId,String lineID,String textOffset){
        Map<String,Object> map=new HashMap<String,Object>();
        int lineNum = Integer.parseInt(lineID);
        int offset = Integer.parseInt(textOffset);
        JSONArray rtn_list = new JSONArray();
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("markID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("markID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            file_num_list.add(Integer.parseInt(file_name[file_name.length - 1]));
        }
        int news_ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        int ID = file_num_list.get(news_ID - 1);
        if(tag != null){
            JSONArray jsonArray = FileIO.readJsonArrayFile(container.DataPath + "/mark/json/"+ID+".json");
            assert jsonArray != null;
            for (int seq_i=0;seq_i<lineNum;seq_i++)rtn_list.add(jsonArray.get(seq_i));
            JSONObject changeTo = new JSONObject();
            JSONObject jsonObject = (JSONObject) jsonArray.get(lineNum);
            assert jsonObject != null;
            changeTo.put("sentence",jsonObject.get("sentence"));
            JSONObject arguments = jsonObject.getJSONObject("arguments");
            JSONArray events = jsonObject.getJSONArray("events");
            JSONObject args = null;
            JSONArray allEvents = null;
            JSONObject newEvent = null;
            JSONObject newItem = new JSONObject();
            newItem.put("text",tag);
            newItem.put("length",tag.length());
            newItem.put("offset",offset);
            boolean sign = true;
            switch (catelogId){
                case "1":
                    args = new JSONObject();
                    JSONArray Times = arguments.getJSONArray("time");
                    JSONArray newTimes = new JSONArray();
                    String time = "";
                    for (Object Time:Times){
                        time = ((JSONObject)Time).get("text").toString();
                        if (time.contains(tag)||(tag.contains(time)&& !time.equals(""))){
                            sign = false;
                            newTimes.add(newItem);
                        }else newTimes.add(Time);
                    }
                    if (sign) newTimes.add(newItem);
                    args.put("time",newTimes);
                    args.put("loc",arguments.get("loc"));
                    args.put("country",arguments.get("country"));
                    args.put("weapon",arguments.get("weapon"));
                    changeTo.put("arguments",args);
                    changeTo.put("events",jsonObject.get("events"));
                    break;
                case "2":
                    args = new JSONObject();
                    JSONArray Locs = arguments.getJSONArray("loc");
                    JSONArray newLocs = new JSONArray();
                    String loc = "";
                    for (Object Loc:Locs){
                        loc = ((JSONObject)Loc).get("text").toString();
                        if (loc.contains(tag)||(tag.contains(loc)&& !loc.equals(""))){
                            sign = false;
                            newLocs.add(newItem);
                        }else newLocs.add(Loc);
                    }
                    if (sign) newLocs.add(newItem);
                    args.put("time",arguments.get("time"));
                    args.put("loc",newLocs);
                    args.put("country",arguments.get("country"));
                    args.put("weapon",arguments.get("weapon"));
                    changeTo.put("arguments",args);
                    changeTo.put("events",jsonObject.get("events"));
                    break;
                case "3":
                    args = new JSONObject();
                    JSONArray Countrys = arguments.getJSONArray("country");
                    JSONArray newCountrys = new JSONArray();
                    String country = "";
                    for (Object Country:Countrys){
                        country = ((JSONObject)Country).get("text").toString();
                        if (country.contains(tag)||(tag.contains(country)&& !country.equals(""))){
                            sign = false;
                            newCountrys.add(newItem);
                        }else newCountrys.add(Country);
                    }
                    if (sign) newCountrys.add(newItem);
                    args.put("time",arguments.get("time"));
                    args.put("loc",arguments.get("loc"));
                    args.put("country",newCountrys);
                    args.put("weapon",arguments.get("weapon"));
                    changeTo.put("arguments",args);
                    changeTo.put("events",jsonObject.get("events"));
                    break;
                case "4":
                    args = new JSONObject();
                    JSONArray Weapons = arguments.getJSONArray("weapon");
                    JSONArray newWeapons = new JSONArray();
                    String weapon = "";
                    for (Object Weapon:Weapons){
                        weapon = ((JSONObject)Weapon).get("text").toString();
                        if (weapon.contains(tag)||(tag.contains(weapon)&& !weapon.equals(""))){
                            sign = false;
                            newWeapons.add(newItem);
                        }else newWeapons.add(Weapon);
                    }
                    if (sign) newWeapons.add(newItem);
                    args.put("time",arguments.get("time"));
                    args.put("loc",arguments.get("loc"));
                    args.put("country",arguments.get("country"));
                    args.put("weapon",newWeapons);
                    changeTo.put("arguments",args);
                    changeTo.put("events",jsonObject.get("events"));
                    break;
                case "5-1":
                    changeTo.put("arguments",jsonObject.get("arguments"));
                    allEvents = new JSONArray();
                    newEvent = new JSONObject();
                    for (Object event:events){
                        String trigger_text = ((JSONObject)event).getJSONObject("trigger").get("text").toString();
                        if (tag.contains(trigger_text)||trigger_text.contains(tag)){
                            sign = false;
                            newEvent.put("subject",((JSONObject) event).get("subject"));
                            newEvent.put("object",((JSONObject) event).get("object"));
                            newEvent.put("trigger",newItem);
                            allEvents.add(newEvent);
                        }else allEvents.add(event);
                    }
                    if (sign){
                        newItem = new JSONObject();
                        newItem.put("text","");
                        newItem.put("length",0);
                        newItem.put("offset",0);
                        newEvent.put("subject",newItem);
                        newItem = new JSONObject();
                        newItem.put("text","");
                        newItem.put("length",0);
                        newItem.put("offset",0);
                        newEvent.put("object",newItem);
                        newItem = new JSONObject();
                        newItem.put("text",tag);
                        newItem.put("length",tag.length());
                        newItem.put("offset",offset);
                        newEvent.put("trigger",newItem);
                        allEvents.add(newEvent);
                    }
                    changeTo.put("events",allEvents);
                    break;
                case "5-2":
                    changeTo.put("arguments",jsonObject.get("arguments"));
                    String subject = null;
                    allEvents = new JSONArray();
                    newEvent = new JSONObject();
                    for (Object event:events){
                        subject = ((JSONObject)event).getJSONObject("subject").get("text").toString();
                        if (subject.contains(tag)||tag.contains(subject)){
                            sign = false;
                            newEvent.put("subject",newItem);
                            newEvent.put("object",((JSONObject) event).get("object"));
                            newEvent.put("trigger",((JSONObject)event).get("trigger"));
                            allEvents.add(newEvent);
                        }else allEvents.add(event);
                    }
                    if (sign){
                        allEvents = new JSONArray();
                        for (int event_i = 1;event_i<events.size();event_i++){
                            JSONObject LAST = (JSONObject)events.get(event_i-1);
                            JSONObject NOW = (JSONObject)events.get(event_i);
                            int subject_offset = NOW.getJSONObject("subject").getInt("offset");
                            int trigger_offset_last = LAST.getJSONObject("trigger").getInt("offset");
                            int trigger_offset = NOW.getJSONObject("trigger").getInt("offset");
                            if (subject_offset>trigger_offset_last&&subject_offset<trigger_offset){
                                if (subject_offset-trigger_offset_last>trigger_offset-subject_offset){
                                    allEvents.add(LAST);
                                    newEvent.put("subject",newItem);
                                    newEvent.put("object",NOW.get("subject"));
                                    newEvent.put("trigger",NOW.get("trigger"));
                                    allEvents.add(newEvent);
                                    event_i += 1;
                                }else {
                                    newEvent.put("subject",newItem);
                                    newEvent.put("object",LAST.get("subject"));
                                    newEvent.put("trigger",LAST.get("trigger"));
                                    allEvents.add(newEvent);
                                }

                            }else allEvents.add(LAST);
                        }
                    }
                    changeTo.put("events",allEvents);
                    break;
                case "5-3":
                    changeTo.put("arguments",jsonObject.get("arguments"));
                    String object = null;
                    allEvents = new JSONArray();
                    newEvent = new JSONObject();
                    for (Object event:events){
                        object = ((JSONObject)event).getJSONObject("object").get("text").toString();
                        if (object.contains(tag)||tag.contains(object)){
                            sign = false;
                            newEvent.put("subject",((JSONObject) event).get("subject"));
                            newEvent.put("object",newItem);
                            newEvent.put("trigger",((JSONObject)event).get("trigger"));
                            allEvents.add(newEvent);
                        }else allEvents.add(event);
                    }
                    if (sign){
                        allEvents = new JSONArray();
                        for (int event_i = 1;event_i<events.size();event_i++){
                            JSONObject LAST = (JSONObject)events.get(event_i-1);
                            JSONObject NOW = (JSONObject)events.get(event_i);
                            int object_offset = NOW.getJSONObject("object").getInt("offset");
                            int trigger_offset_last = LAST.getJSONObject("trigger").getInt("offset");
                            int trigger_offset = NOW.getJSONObject("trigger").getInt("offset");
                            if (object_offset>trigger_offset_last&&object_offset<trigger_offset){
                                if (object_offset-trigger_offset_last>trigger_offset-object_offset){
                                    allEvents.add(LAST);
                                    newEvent.put("subject",NOW.get("subject"));
                                    newEvent.put("object",newItem);
                                    newEvent.put("trigger",NOW.get("trigger"));
                                    allEvents.add(newEvent);
                                    event_i += 1;
                                }else {
                                    newEvent.put("subject",LAST.get("subject"));
                                    newEvent.put("object",newItem);
                                    newEvent.put("trigger",LAST.get("trigger"));
                                    allEvents.add(newEvent);
                                }

                            }else allEvents.add(LAST);
                        }
                    }
                    changeTo.put("events",allEvents);
                    break;
                default:
                    break;
            }
            rtn_list.add(changeTo);
            for (int seq_i=lineNum+1;seq_i<jsonArray.size();seq_i++)rtn_list.add(jsonArray.get(seq_i));
            FileIO.writeFileAll(container.DataPath + "/mark/json/"+ID+".json",rtn_list.toString());
            map.put("result","ok");
        }else map.put("result","error");
        return map;
    }
    @RequestMapping("/general/human/refresh")
    @ResponseBody
    public void refreshJSON(HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("markID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("markID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            file_num_list.add(Integer.parseInt(file_name[file_name.length - 1]));
        }
        int news_ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        int ID = file_num_list.get(news_ID - 1);
        FileIO.removeFile(container.DataPath+"/mark/json/"+ ID + ".json");
    }
    @RequestMapping("/general/human/delete")
    @ResponseBody
    public void deleteJSON(HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("markID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("markID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        String basePath=container.DataPath + "/mark/txt/";
        file_num_list = new ArrayList<>();
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            file_num_list.add(Integer.parseInt(file_name[file_name.length - 1]));
        }
        int news_ID = pageID.equals("") ? 1 : Integer.parseInt(pageID);
        int ID = file_num_list.get(news_ID - 1);
        FileIO.removeFile(container.DataPath+"/mark/json/"+ ID + ".json");
        FileIO.removeFile(container.DataPath+"/mark/txt/"+ ID + ".txt");
        FileIO.removeFile(container.DataPath+"/mark/txt_lines/"+ ID + ".txt");
        this.file_list= new File(basePath).list();
    }
    @RequestMapping("/general/human/download")
    @ResponseBody
    public void downloadJSON(HttpServletResponse response, HttpServletRequest request) throws IOException{
        JSONArray examples = null;
        JSONArray loadJson = new JSONArray();
        String basePath=container.DataPath + "/mark/txt/";
        for(String file_:file_list){
            String[] file_name = (file_.split(".txt")[0]).split("/");
            examples = FileIO.readJsonArrayFile(basePath + file_name[file_name.length - 1] + ".json");
            if (examples!=null)
                loadJson.addAll(examples);
        }
        FileIO.writeFileAll(container.ExamplePath + "/train.json", loadJson.toString());
        String fileName = "train.json";
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
            in = new FileInputStream(container.ExamplePath+"/"+fileName);
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
    @RequestMapping("/general/extraction")
    public String extractionCenter(Model model, HttpSession session){
        return "backstage/general/manage/extraction";
    }
    @RequestMapping("/general/system")
    public String Systemlog(Model model, HttpSession session){
        return "backstage/general/logs/system_page";
    }
    @RequestMapping("/general/server")
    public String Serverlog(Model model, HttpSession session){
        return "backstage/general/logs/servlet_page";
    }
    @RequestMapping("/general/action")
    public String Actionlog(Model model, HttpSession session){
        return "backstage/general/logs/system_page";
    }
    @RequestMapping("/general/email")
    public String EmailMess(Model model, HttpSession session){
        return "backstage/general/message/Email_page";
    }
    @RequestMapping("/general/feedback")
    public String FeedBackMess(Model model, HttpSession session){
        return "backstage/general/message/feedback_page";
    }
    @RequestMapping("/others/load")
    public String upload(Model model, HttpSession session){
        return "backstage/general/message/feedback_page";
    }
    @RequestMapping("/others/load/file")
    @ResponseBody
    public JSONObject uploadfile(@RequestParam(value = "myfile",required=false) MultipartFile file){
        Map<String,Object> map=new HashMap<String,Object>();
        if (!file.isEmpty()) {
            String originalFilename = file.getOriginalFilename();
            long size = file.getSize();
            System.out.println("上传文件名为" + originalFilename + ",上传大小为" + size);
            //uuid是机器码，是唯一的
            String uuid = UUID.randomUUID().toString();
            //获取后缀名
            int lastIndexOf = originalFilename.lastIndexOf(".");
            String substring = originalFilename.substring(lastIndexOf);
            //设置保存路径
            String filenames = container.ImgPath + "/" + uuid + substring;
            String url="/img/"+uuid+substring;
            File files = new File(filenames);
            try {
                //以绝对路径保存重名命后的图片
                file.transferTo(files);
                map.put("imgurl",url);
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
    @RequestMapping("/others/config")
    public String ConfigChange(Model model, HttpSession session){
        return "backstage/others/professional/change_config_page";
    }
    @RequestMapping("/others/crawler")
    public String CrawlerChange(Model model, HttpSession session){
        return "backstage/others/professional/change_crawler_page";
    }
}
