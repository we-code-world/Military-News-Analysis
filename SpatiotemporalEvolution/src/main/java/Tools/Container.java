package Tools;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Container {
    public String baiduMapAK;
    public String googleMapAK;
    public String[] MapData = {"北京市","天津市", "上海市","重庆市", "河北省",
            "河南省", "云南省","辽宁省", "黑龙江省","湖南省", "安徽省","山东省",
            "新疆维吾尔自治区","江苏省","浙江省","江西省","湖北省","广西壮族自治区",
            "甘肃省","山西省","内蒙古自治区","陕西省","吉林省","福建省","贵州省",
            "广东省","青海省","西藏自治区","四川省","宁夏回族自治区","海南省",
            "台湾省","香港特别行政区","澳门特别行政区","南海"};
    public String ConfPath;
    public String RootPath;
    public String ServletPath;
    public String DataPath;
    public String ExamplePath;
    public String PyPath;
    public String ResPath;
    public String MapPath;
    public String ImgPath;
    public String TempPath;
    public List<String> EventClasses;
    public Container(){
        this("/usr/local/Rootpath/conf");
    }
    public Container(String confurl){
        ConfPath = confurl;
        RootPath = "E:/Rootpath"; // 本地路径
        ServletPath = "D:/intelliJ/SpatiotemporalEvolution/src/main/webapp"; // 服务器路径
        DataPath = RootPath+"/data";
        ExamplePath = RootPath+"/dataset";
        PyPath = RootPath+"/bin";
        ResPath = RootPath+"/resource";
        MapPath = ServletPath + "/json/world";
        TempPath = RootPath+"/temp";
        ImgPath = ServletPath + "/img";
        String[] event = {"accidentevent",
                "conflictevent",
                "practiceevent",
                "provocativeevent",
                "rdevent",
                "transactionevent"
        };
        EventClasses = Arrays.asList(event);
        baiduMapAK="wUixKXpRjjTuNebaEib9FfGxvjDuoPjG";
        googleMapAK="AIzaSyAQ-LCGlyvahNSP6-VezsWyEsupKAMr-sc";
        String fileName = confurl+"/context.txt";
        List<String> list = FileIO.readFileByLines(fileName);
        for (String strs:list){
            //去除注释
            String str_1 = strs.split("#")[0];
            if (!str_1.contains("="))continue;
            //System.out.println(str_1);
            //分割名称和值
            String[] nv = str_1.split("=");
            String name = nv[0].replaceAll("\r\n|\r|\n| |\t", "");
            String value = nv[1].replaceAll("\r\n|\r|\n| |\t", "");
            switch (name) {
                case "baiduAK":
                    //System.out.println(value);
                    baiduMapAK = value;
                    break;
                case "googleAK":
                    //System.out.println(value);
                    googleMapAK = value;
                    break;
                case "RootPath":
                    //System.out.println(value);
                    RootPath = value;
                    break;
                case "ServletPath":
                    //System.out.println(value);
                    ServletPath = value;
                    break;
                case "DataPath":
                    if (value.contains("%RootPath%")){
                        DataPath = value.replaceAll("%RootPath%",RootPath);
                    }else
                        //System.out.println(value);
                        DataPath = value;
                    break;
                case "ExamplePath":
                    if (value.contains("%RootPath%")){
                        ExamplePath = value.replaceAll("%RootPath%",RootPath);
                    }else
                        //System.out.println(value);
                        ExamplePath = value;
                    break;
                case "PyPath":
                    if (value.contains("%RootPath%")){
                        PyPath = value.replaceAll("%RootPath%",RootPath);
                    }else
                    //System.out.println(value);
                    PyPath = value;
                    break;
                case "ResPath":
                    if (value.contains("%RootPath%")){
                        ResPath = value.replaceAll("%RootPath%",RootPath);
                    }else
                    //System.out.println(value);
                    ResPath = value;
                    break;
                case "MapPath":
                    if (value.contains("%ServletPath%")){
                        MapPath = value.replaceAll("%ServletPath%",ServletPath);
                    }else
                        //System.out.println(value);
                        ImgPath = value;
                    break;
                case "TempPath":
                    if (value.contains("%RootPath%")){
                        TempPath = value.replaceAll("%RootPath%",RootPath);
                    }else
                        //System.out.println(value);
                        TempPath = value;
                    break;
                case "ImgPath":
                    if (value.contains("%RootPath%")){
                        ImgPath = value.replaceAll("%RootPath%",RootPath);
                    }else
                        //System.out.println(value);
                        ImgPath = value;
                    break;
                case "EventClasses":
                    //System.out.println(value);
                    String[] ets = value.split("'");
                    List<String> events = new ArrayList<>();
                    for (String stri :ets){
                        if (stri.contains("event")){
                            events.add(stri);
                        }
                    }
                    EventClasses = events;
                    break;
                default:
                    break;
            }
        }
    }
//    public static void main(String str[]){
//        Container container = new Container();
//    }
}
