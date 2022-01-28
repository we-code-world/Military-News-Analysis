package Service;

import DAO.NewsMapper;
import Entity.News;
import com.github.pagehelper.PageInfo;

public interface NewsService {
    void setNewsMapper(NewsMapper newsMapper);

    //分页查找所有用户
    News findByID(int pageID);

    //分页查找所有新闻
    PageInfo<News> pageAll(int pageNum, int pageSize);
}
