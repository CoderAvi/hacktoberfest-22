package step.learning.filters;

import com.google.inject.Singleton;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

//@WebFilter("/*")
@Singleton
public class CharsetFilter implements Filter {
    private FilterConfig filterConfig;
    public void init(FilterConfig filterConfig) throws ServletException {
        this.filterConfig = filterConfig;
    }
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        servletResponse.setCharacterEncoding("UTF-8");
        servletResponse.setContentType("text/html; charset=UTF-8");
        servletRequest.setCharacterEncoding("UTF-8");
        servletRequest.setAttribute("from-charset-filter", "Charset filter works!!");
        filterChain.doFilter(servletRequest, servletResponse);
    }
    public void destroy() {
        filterConfig = null;
    }
}
