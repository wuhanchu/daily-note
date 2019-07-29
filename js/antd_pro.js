// 页面跳转
import { routerRedux } from "dva/router";

this.props.dispatch(
  routerRedux.push({
    pathname: "/giveData/queryOrder",
    params: record.userId
  })
);
