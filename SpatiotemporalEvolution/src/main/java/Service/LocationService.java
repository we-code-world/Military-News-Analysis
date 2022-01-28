package Service;

import DAO.LocationMapper;
import Entity.Location;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public interface LocationService {
    void setLocationMapper(LocationMapper locationMapper);

    //分页查找所有用户
    PageInfo<Location> pageAll(int pageNum, int pageSize);

    //查找所有事件中出现的地点
    JSONObject getLocationsInEvent(JSONObject Locs,String ConName,int level);
}
