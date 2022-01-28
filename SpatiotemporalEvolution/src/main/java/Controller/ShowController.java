package Controller;

import Annotation.AccessLimit;
import Entity.*;
import Service.*;
import Tools.Container;
import Tools.CreatePDF;
import Tools.DateUtils;
import Tools.FileIO;
import com.github.pagehelper.PageInfo;
import com.lowagie.text.DocumentException;
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


//事件展示相关操作
@Controller
@RequestMapping("/Show")
public class ShowController {
    @Autowired
    @Qualifier("NewsServiceImpl")
    private NewsService newsService;
    @Autowired
    @Qualifier("EventServiceImpl")
    private EventService eventService;
    @Autowired
    @Qualifier("WeaponServiceImpl")
    private WeaponService weaponService;
    @Autowired
    @Qualifier("MessageServiceImpl")
    private MessageService messageService;
    @Autowired
    @Qualifier("LocationServiceImpl")
    private LocationService locationService;
    public Container container = new Container();
    @RequestMapping("/logout")
    public String Logout(HttpSession session){
        session.removeAttribute("userInfo");
        return "return/Refresh";
    }
    //跳转到容器页面
    @RequestMapping("/Container")
    public String getContainer(Model model, HttpSession session){
        User user = (User) session.getAttribute("userInfo");
        model.addAttribute("username",user.getUserName());
        model.addAttribute("userFace",user.getPhoto());
        return "front_end/container";
    }
    //跳转到内部容器页面
    @RequestMapping("/Event")
    public String getEvent(Model model, HttpSession session){
        User user = (User) session.getAttribute("userInfo");
        model.addAttribute("username",user.getUserName());
        return "front_end/event/event_list";
    }
    //获取新闻信息
    @RequestMapping("/News")
    public String getNewsByTime(Model model, HttpServletRequest request, HttpServletResponse response){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_num = new Cookie("pageNum","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageNum")){
                cookie_num=ck;
            }
        }
        String pageNum = cookie_num.getValue();
        int num = pageNum.equals("") ? 1 : Integer.parseInt(pageNum);
        cookie_num.setValue(""+num);
        response.addCookie(cookie_num);
        PageInfo<News> pageNews = newsService.pageAll(num,15);
        model.addAttribute("pageDetil",pageNews);
        return "front_end/news/news_list";
    }
    //获取新闻数据展示页面
    @RequestMapping("/News/Source")
    public String getNewsBySource(Model model){
        return "front_end/news/news_source";
    }
    //获取新闻信息
    @RequestMapping("/News/Detail")
    public String getNewsDetail(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_ID = new Cookie("pageID","");
        for (Cookie ck:cookies){
            if (ck.getName().equals("pageID")){
                cookie_ID=ck;
            }
        }
        String pageID = cookie_ID.getValue();
        int ID = cookie_ID.getValue().equals("")? 1: Integer.parseInt(pageID);
        News ns = newsService.findByID(ID);
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
                    KeySentence ks = weaponService.getAllKeySentencesByNewsIDAndNum(ID,j);
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
        List<KeySentence> kss = weaponService.getAllKeySentencesByNewsID(ID);
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
        return "front_end/news/news_page";
    }
    //获取新闻信息
    @RequestMapping("/News/Detail/submit")
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
            messageService.create(tag,user.getUserid(),ID,catelogid);
            map.put("result","ok");
        }else map.put("result","error");
        return map;
    }
    //获取武器装备
    @RequestMapping("/Weapons")
    public String getWeaponsByNameNew(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        Cookie cookie_wea = new Cookie("weapon","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
                case "weapon":
                    cookie_wea = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"world" : location;
        JSONArray weaponIDS = eventService.getAllWeaponIDClass(cookie_start.getValue(),cookie_end.getValue());
        JSONObject jsonObject;
        model.addAttribute("location",location);
        model.addAttribute("WeaponJson",weaponService.getClassAndSClassInEvent(weaponIDS));
        jsonObject = new JSONObject();
        jsonObject.put("data",weaponService.getAllClass());
        model.addAttribute("ClassJson",jsonObject);
        model.addAttribute("SClassJson",weaponService.getClassObj());
        return "front_end/event/weaponClass/weapon_analysis";
    }
    //获取武器装备
    @RequestMapping("/Weapons/Old")
    public String getWeaponsByNameOld(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"world" : location;
        JSONObject ClassJson = new JSONObject();
        JSONObject jsonObject;
        for (String Class:weaponService.getAllClass()) {
            int[] countClass = {0,0,0,0,0,0};
            int rtn_countClass = 0;
            for (String SClass:weaponService.getAllSClass(Class)) {
                List<Weapon> weaponList = weaponService.getAllWeaponsBySClass(SClass);
                int rtn_countSClass=0;
                int[] countSClass = eventService.getCountBySClass(weaponList,cookie_start.getValue(),cookie_end.getValue());
                for (int mi=0;mi<6;mi++) {
                    countClass[mi]+=countSClass[mi];
                    rtn_countSClass+=countSClass[mi];
                }
                jsonObject = new JSONObject();
                jsonObject.put(SClass,rtn_countSClass);
                ClassJson.put(SClass,rtn_countSClass);
            }
            for (int mi=0;mi<6;mi++) {
                rtn_countClass+=countClass[mi];
            }
            ClassJson.put(Class,rtn_countClass);
        }
        model.addAttribute("location",location);
        model.addAttribute("WeaponJson",ClassJson);
        jsonObject = new JSONObject();
        jsonObject.put("data",weaponService.getAllClass());
        model.addAttribute("ClassJson",jsonObject);
        model.addAttribute("SClassJson",weaponService.getClassObj());
        return "front_end/event/weaponClass/weapon_analysis";
    }
    //获取事件发展展示页面
    @RequestMapping("/download.pdf")
    @ResponseBody
    public void myDownLoad(HttpServletResponse response, HttpServletRequest request) throws IOException, DocumentException {
        String fileName="download.pdf",encoding="GBK";
        String filePath=container.TempPath + "/" +fileName;
        CreatePDF.createPdfFile(filePath);
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
            response.setHeader("Content-disposition", "attachment; filename="+fileName);
        } catch (UnsupportedEncodingException e) {
            System.out.println(e.getMessage());
        }
        InputStream in = null;
        OutputStream out = null;
        try {
            //获取要下载的文件输入流
            in = new FileInputStream(filePath);
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
                CreatePDF.delPdfFile(filePath);
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    //获取三维地图热点展示页面
    @RequestMapping("/Location")
    public String getlocation(Model model){
        return "front_end/event/event_location";
    }
    //获取地图展示
    @RequestMapping("/Map2d")
    @AccessLimit(seconds = 20,maxCount = 5)
    public String get2dMap(Model model, HttpSession session, HttpServletRequest request) throws FileNotFoundException, UnsupportedEncodingException {
        User user = (User) session.getAttribute("userInfo");
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location_map","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location_map":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        JSONObject world_mapping = FileIO.readJsonFile(container.MapPath+"/world-mapping.json");
        JSONObject Country_map;
        String ConName = "";
        assert world_mapping != null;
        int level = 0;
        List<String> loc_names = new ArrayList<>();
        if (location.equals("")||location.equals("world")){
            level = 1;
            model.addAttribute("location", "world" );
            model.addAttribute("location_file","world");
            for (Object entry: world_mapping.entrySet()) {
                loc_names.add(((Map.Entry<String,JSONObject>) entry).getKey());
            }
        }else{
            level = 2;
            location = location.replaceAll("%20"," ");
            Country_map = world_mapping.getJSONObject(location);
            String fileName = Country_map.getString("mapFileName");
            ConName = Country_map.getString("cn");
            model.addAttribute("location", location);
            model.addAttribute("location_file", fileName);
            JSONArray country_mapping = FileIO.readJsonArrayFile(container.MapPath + "/mapping/"+fileName+"-mapping.json");
            assert country_mapping != null;
            for(int i = 0; i < country_mapping.size(); i ++) {
                JSONObject loc_name = (JSONObject) country_mapping.get(i);
                loc_names.add((String) loc_name.get("name"));
            }
        }
        model.addAttribute("username",user.getUserName());
        JSONArray MapValue = eventService.getMapValue(cookie_start.getValue(),cookie_end.getValue());
        Map<String,Integer> mapData = new HashMap<>();
        JSONObject jsonObject;
        for (int i=0;i<loc_names.size();i++){
            mapData.put(loc_names.get(i),0);
        }
        jsonObject = new JSONObject();
        jsonObject.put("mapValue",MapValue);
        jsonObject.put("mapData",mapData);
        jsonObject.put("maxValue",0);
        JSONObject locs = locationService.getLocationsInEvent(jsonObject,ConName,level);
        model.addAttribute("mapdata",locs.get("mapData"));
        model.addAttribute("maxValue",locs.get("maxValue"));
        return "front_end/event/map/2dmap";
    }
    //获取三维地图热点展示页面
    @RequestMapping("/Map3d")
    public String get3dmap(Model model){
        return "front_end/event/map/3dmap-time";
    }
    //获取谷歌地图热点展示页面
    @RequestMapping("/Mapgoogle")
    public String getgooglemap(Model model){
        return "front_end/event/map/googlemap";
    }
    //获取百度地图热点展示页面
    @RequestMapping("/Mapbaidu")
    public String getbaidumap(Model model){
        return "front_end/event/map/baidumap";
    }
    @RequestMapping("/Mapbaidu/getdata")
    @ResponseBody
    public Map<String,Object> getMapData(int catelogid,@Param("weaponSClass") String weaponSClass,@Param("weaponClass") String weaponClass){
        Map<String,Object> map=new HashMap<String,Object>();
        JSONArray data_jsonArray = new JSONArray();
        JSONObject jsonObject;
        JSONArray Map_jsonArray = new JSONArray();
        map.put("loc_data",data_jsonArray);
        map.put("loc_Map",Map_jsonArray);
        map.put("result","ok");
        //map.put("result","error");
        return map;
    }
    //获取首页展示
    @RequestMapping("/index")
    public String showIndex(Model model,HttpSession session){
        User user = (User) session.getAttribute("userInfo");
        model.addAttribute("username",user.getUserName());
        return "front_end/inner_index";
    }
    //获取图表分析页面
    @RequestMapping("/analysis")
    public String getanalysis(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"world" : location;
        model.addAttribute("location",location);
        JSONArray jsonPie = new JSONArray();
        JSONArray jsondia = new JSONArray();
        List<String> arraylegend = eventService.getLegend();
        JSONArray jsonLegend = new JSONArray();
        jsonLegend.addAll(Arrays.asList(arraylegend));
        String[] arraytime = DateUtils.getMonthList(cookie_start.getValue(), cookie_end.getValue()).toArray(new String[0]);
        JSONArray jsonTime = new JSONArray();
        jsonTime.addAll(Arrays.asList(arraytime));
        JSONArray jsondata = new JSONArray();
        JSONObject jsonObject;
        model.addAttribute("piedata",jsonPie);
        for (Link link:eventService.getBriefLinks()){
            jsonObject = new JSONObject();
            jsonObject.put("source",link.source);
            jsonObject.put("target",link.target);
            jsondia.add(jsonObject);
        }
        model.addAttribute("dialink",jsondia);
        model.addAttribute("legend_data",jsonLegend);
        model.addAttribute("time_data",jsonTime);
        for (String legend_name:arraylegend){
            jsonObject = new JSONObject();
            jsonObject.put("name",legend_name);
            jsonObject.put("type","bar");
            jsondata.add(jsonObject);
        }
        model.addAttribute("_data_",jsondata);
        return "front_end/event/event_analysis";
    }
    //获取图表分析页面
    @RequestMapping("/weapon_event")
    public String getWeapon_Event(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"全球" : location;
        List<String> arraytime = DateUtils.getYearList(cookie_start.getValue(), cookie_end.getValue());
        model.addAttribute("yearArray",arraytime);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("practice",eventService.getPracticeEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("transaction",eventService.getTransactionEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("conflict",eventService.getConflictEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("RD",eventService.getRDEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("accident",eventService.getAccidentEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("provocative",eventService.getProvocativeEvents(cookie_start.getValue(), cookie_end.getValue()));
        model.addAttribute("location",location);
        model.addAttribute("dataMap",jsonObject);
        return "front_end/event/weapon_event";
    }
    @RequestMapping("/weapon_event/getdata")
    @ResponseBody
    public Map<String,Object> getWeaponEventData(HttpServletRequest request,int catelogid,@Param("weaponSClass") String weaponSClass,@Param("weaponClass") String weaponClass){
        Map<String,Object> map=new HashMap<String,Object>();
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"world" : location;
        List<String> arraytime = DateUtils.getYearList(cookie_start.getValue(), cookie_end.getValue());
        map.put("yearArray",arraytime);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("practice",eventService.getPracticeEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("transaction",eventService.getTransactionEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("conflict",eventService.getConflictEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("RD",eventService.getRDEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("accident",eventService.getAccidentEvents(cookie_start.getValue(), cookie_end.getValue()));
        jsonObject.put("provocative",eventService.getProvocativeEvents(cookie_start.getValue(), cookie_end.getValue()));
        map.put("location",location);
        map.put("dataMap",jsonObject);
        map.put("result","ok");
        return map;
    }
    //获取事件发展展示页面
    @RequestMapping("/event_weapon")
    public String getdevelop(Model model,HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        Cookie cookie_loc = new Cookie("location","");
        Cookie cookie_start = new Cookie("start_time","");
        Cookie cookie_end = new Cookie("end_time","");
        for (Cookie ck:cookies){
            switch (ck.getName()) {
                case "location":
                    cookie_loc = ck;
                    break;
                case "start_time":
                    cookie_start = ck;
                    break;
                case "end_time":
                    cookie_end = ck;
                    break;
            }
        }
        String location = cookie_loc.getValue();
        location = location.equals("") ?"world" : location;
        List<TimePointer> timePointers = eventService.getTimePointers(cookie_start.getValue(),cookie_end.getValue());
        model.addAttribute("time_point",timePointers);
        model.addAttribute("location",location);
        return "front_end/event/event_weapon";
    }
    @RequestMapping("/event_weapon/getdata")
    @ResponseBody
    public Map<String,Object> getEventWeaponData(@Param("ChartName")String ChartName,@Param("dataClass") String dataClass){
        Map<String,Object> map=new HashMap<String,Object>();
        JSONArray data_jsonArray = new JSONArray();
        JSONArray jsonLinks = new JSONArray();
        JSONObject jsonObject;
        for (Link link:eventService.getLinks()){
            jsonObject = new JSONObject();
            jsonObject.put("source",link.source);
            jsonObject.put("target",link.target);
            jsonLinks.add(jsonObject);
        }
        map.put("eventLables",eventService.getLegend());
        map.put("datalink",jsonLinks);
        map.put("result","ok");
        //map.put("result","error");
        return map;
    }
    //获取武器分类展示页面
    @RequestMapping("/weapon_class")
    public String getWeaponlass(Model model){
        JSONArray jsonNodes = new JSONArray();
        JSONArray jsonLinks = new JSONArray();
        JSONArray jsonCategories = new JSONArray();
        JSONObject jsonObject;
        Queue<Section> queue_sec =  new LinkedList<>();
        queue_sec.offer(new Section(0,2000,"","",0));
        int startNum = 1;
        List<String> weaponClass = weaponService.getAllClass();
        for (String cate:weaponClass) {
            jsonObject = new JSONObject();
            jsonObject.put("name",cate);
            jsonCategories.add(jsonObject);
        }
        Section section = queue_sec.poll();
        assert section != null;
        List<Section> sections_child = section.getRootChild(weaponClass,startNum);
        startNum += weaponClass.size();
        List<Section> weapon_sections = new ArrayList<>();
        for (Section s:sections_child) {
            queue_sec.offer(s);
            jsonObject = new JSONObject();
            jsonObject.put("id",""+s.id);
            jsonObject.put("name",s.name);
            jsonObject.put("symbolSize",5);
            jsonObject.put("x",s.point);
            jsonObject.put("y",0);
            jsonObject.put("value",new Random().ints(1000));
            jsonObject.put("category",s.category);
            jsonNodes.add(jsonObject);
        }
        while (!queue_sec.isEmpty()){
            section = queue_sec.poll();
            List<String> weaponSClass = weaponService.getAllSClass(section.name);
            sections_child = section.getChild(weaponSClass,startNum);
            for (Link link:section.getLinks(weaponSClass,startNum)){
                jsonObject = new JSONObject();
                jsonObject.put("source",link.source);
                jsonObject.put("target",link.target);
                jsonLinks.add(jsonObject);
            }
            startNum += weaponSClass.size();
            weapon_sections.addAll(sections_child);
        }
        for (Section s:weapon_sections) {
            queue_sec.offer(s);
            jsonObject = new JSONObject();
            jsonObject.put("id",""+s.id);
            jsonObject.put("name",s.name);
            jsonObject.put("symbolSize",5);
            jsonObject.put("x",s.point);
            jsonObject.put("y",400);
            jsonObject.put("value",new Random().ints(100));
            jsonObject.put("category",s.category);
            jsonNodes.add(jsonObject);
        }
        weapon_sections = new ArrayList<>();
        while (!queue_sec.isEmpty()){
            section = queue_sec.poll();
            List<String> weaponsList = weaponService.getAllWeapons(section.name);
            sections_child = section.getChild(weaponsList,startNum);
            for (Link link:section.getLinks(weaponsList,startNum)){
                jsonObject = new JSONObject();
                jsonObject.put("source",link.source);
                jsonObject.put("target",link.target);
                jsonLinks.add(jsonObject);
            }
            startNum += weaponsList.size();
            weapon_sections.addAll(sections_child);
        }
        for (Section s:weapon_sections) {
            queue_sec.offer(s);
            jsonObject = new JSONObject();
            jsonObject.put("id",""+s.id);
            jsonObject.put("name",s.name);
            jsonObject.put("symbolSize",5);
            jsonObject.put("x",s.point);
            jsonObject.put("y",1200);
            jsonObject.put("value",new Random().ints(10));
            jsonObject.put("category",s.category);
            jsonNodes.add(jsonObject);
        }
        model.addAttribute("links",jsonLinks);
        model.addAttribute("nodes",jsonNodes);
        model.addAttribute("categories",jsonCategories);
        return "front_end/event/weaponClass/weaponClasses";
    }
    @RequestMapping("/photoImg/load")
    @ResponseBody
    public JSONObject uploadImg(@RequestParam(value = "myfile",required=false) MultipartFile file){
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
            String filenames = container.ImgPath + uuid + substring;
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
}
