package Service;

import DAO.LocationMapper;
import Entity.Location;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.util.List;
import java.util.Map;
import java.util.Random;

public class LocationServiceImpl implements LocationService{
    private LocationMapper locationMapper;

    public void setLocationMapper(LocationMapper locationMapper) {
        this.locationMapper = locationMapper;
    }

    @Override
    public PageInfo<Location> pageAll(int pageNum, int pageSize) {
        PageHelper.startPage(pageNum,pageSize);
        List<Location> list = locationMapper.findAll();
        PageInfo<Location> page = new PageInfo<>(list);
        return page;
    }

    @Override
    public JSONObject getLocationsInEvent(JSONObject Locs,String ConName,int level) {
        JSONObject res_map = new JSONObject();
        JSONArray MapVlaue = Locs.getJSONArray("mapValue");
        Map<String,Integer> MapData = (Map<String,Integer>)Locs.get("mapData");
        if (level == 1){
            for (Object entry : MapVlaue){
                String nameID = ((JSONObject)entry).getString("ID");
                int Number = ((JSONObject)entry).getInt("NUMBER");
                Location location = locationMapper.findByID(Integer.parseInt(nameID));
                String Country = location.getCountry();
                if (Country!=null&&MapData.containsKey(Country)&&location.getLevel()!=0)
                    MapData.put(Country,MapData.get(Country)+Number);
            }
        }else {
            for (Object entry : MapVlaue){
                String nameID = ((JSONObject)entry).getString("ID");
                int Number = ((JSONObject)entry).getInt("NUMBER");
                Location location = locationMapper.findByID(Integer.parseInt(nameID));
                String City = location.getStandardPos();
                if (City!=null&&MapData.containsKey(City)&&location.getLevel()!=0)
                    MapData.put(City,MapData.get(City)+Number);
            }
        }
        JSONArray mapData = new JSONArray();
        JSONObject Data;
        int MaxValue = 0;
        for (Map.Entry<String, Integer> entry:MapData.entrySet()){
            Data = new JSONObject();
            int number = entry.getValue()+ (int)(Math.random()*600);
            if (number>MaxValue)MaxValue = number;
            Data.put("name",entry.getKey());
            Data.put("value",number);
            mapData.add(Data);
        }
        res_map.put("mapData",mapData);
        res_map.put("maxValue",MaxValue);
        return res_map;
    }
}
