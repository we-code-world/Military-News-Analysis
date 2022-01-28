package Service;

import DAO.NewsMapper;
import Entity.News;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;

import java.util.List;

public class NewsServiceImpl implements NewsService {
    private NewsMapper newsMapper;

    public void setNewsMapper(NewsMapper newsMapper) {
        this.newsMapper = newsMapper;
    }

    @Override
    public News findByID(int pageID) {
        return newsMapper.findByID(pageID);
    }

    @Override
    public PageInfo<News> pageAll(int pageNum, int pageSize) {
        PageHelper.startPage(pageNum,pageSize);
        List<News> list = newsMapper.findAll();
        PageInfo<News> page = new PageInfo<>(list);
        return page;
    }
}
