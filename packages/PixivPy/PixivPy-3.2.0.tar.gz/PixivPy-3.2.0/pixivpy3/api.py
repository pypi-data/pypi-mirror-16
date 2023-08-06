# -*- coding:utf-8 -*-

import os
import sys
import shutil
import json
import requests

from .utils import PixivError, JsonDict


class BasePixivAPI(object):
    access_token = None
    user_id = 0
    refresh_token = None

    def __init__(self, **requests_kwargs):
        """initialize requests kwargs if need be"""
        self.requests_kwargs = requests_kwargs

    def parse_json(self, json_str):
        """parse str into JsonDict"""

        def _obj_hook(pairs):
            """convert json object to python object"""
            o = JsonDict()
            for k, v in pairs.items():
                o[str(k)] = v
            return o

        return json.loads(json_str, object_hook=_obj_hook)

    def require_auth(self):
        if self.access_token is None:
            raise PixivError('Authentication required! Call login() or set_auth() first!')

    def requests_call(self, method, url, headers={}, params=None, data=None, stream=False):
        """ requests http/https call for Pixiv API """
        try:
            if (method == 'GET'):
                return requests.get(url, params=params, headers=headers, stream=stream, **self.requests_kwargs)
            elif (method == 'POST'):
                return requests.post(url, params=params, data=data, headers=headers, stream=stream, **self.requests_kwargs)
            elif (method == 'DELETE'):
                return requests.delete(url, params=params, data=data, headers=headers, stream=stream, **self.requests_kwargs)
        except Exception as e:
            raise PixivError('requests %s %s error: %s' % (method, url, e))

        raise PixivError('Unknow method: %s' % method)

    def set_auth(self, access_token, refresh_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token

    def login(self, username, password):
        return self.auth(username=username, password=password)

    def auth(self, username=None, password=None, refresh_token=None):
        """Login with password, or use the refresh_token to acquire a new bearer token"""

        url = 'https://oauth.secure.pixiv.net/auth/token'
        headers = {
            'App-OS': 'ios',
            'App-OS-Version': '9.3.3',
            'App-Version': '6.0.9',
            'User-Agent': 'PixivIOSApp/6.0.9 (iOS 9.3.3; iPhone8,1)',
        }
        data = {
            'get_secure_url': 1,
            'client_id': 'bYGKuGVw91e0NMfPGp44euvGt59s',
            'client_secret': 'HP3RmkgAmEGro0gn1x9ioawQE8WMfvLXDz3ZqxpK',
        }

        if (username is not None) and (password is not None):
            data['grant_type'] = 'password'
            data['username'] = username
            data['password'] = password
        elif (refresh_token is not None) or (self.refresh_token is not None):
            data['grant_type'] = 'refresh_token'
            data['refresh_token'] = refresh_token or self.refresh_token
        else:
            raise PixivError('[ERROR] auth() but no password or refresh_token is set.')

        r = self.requests_call('POST', url, headers=headers, data=data)
        if (r.status_code not in [200, 301, 302]):
            if data['grant_type'] == 'password':
                raise PixivError('[ERROR] auth() failed! check username and password.\nHTTP %s: %s' % (r.status_code, r.text), header=r.headers, body=r.text)
            else:
                raise PixivError('[ERROR] auth() failed! check refresh_token.\nHTTP %s: %s' % (r.status_code, r.text), header=r.headers, body=r.text)

        token = None
        try:
            # get access_token
            token = self.parse_json(r.text)
            self.access_token = token.response.access_token
            self.user_id = token.response.user.id
            self.refresh_token = token.response.refresh_token
        except:
            raise PixivError('Get access_token error! Response: %s' % (token), header=r.headers, body=r.text)

        # return auth/token response
        return token

    def download(self, url, prefix='', path=None, referer='https://app-api.pixiv.net/'):
        """Download image to file (use 6.0 app-api)"""
        if (not path):
            path = prefix + os.path.basename(url)
        # Write stream to file
        response = self.requests_call('GET', url, headers={ 'Referer': referer }, stream=True)
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

# Public-API
class PixivAPI(BasePixivAPI):

    def __init__(self, **requests_kwargs):
        """initialize requests kwargs if need be"""
        super(PixivAPI, self).__init__(**requests_kwargs)

    # Check auth and set BearerToken to headers
    def auth_requests_call(self, method, url, headers={}, params=None, data=None):
        self.require_auth()
        headers['Referer'] = 'http://spapi.pixiv.net/'
        headers['User-Agent'] = 'PixivIOSApp/5.8.7'
        headers['Authorization'] = 'Bearer %s' % self.access_token
        return self.requests_call(method, url, headers, params, data)

    def parse_result(self, req):
        try:
            return self.parse_json(req.text)
        except Exception as e:
            raise PixivError("parse_json() error: %s" % (e), header=req.headers, body=req.text)

    def bad_words(self):
        url = 'https://public-api.secure.pixiv.net/v1.1/bad_words.json'
        r = self.auth_requests_call('GET', url)
        return self.parse_result(r)

    # 作品详细
    def works(self, illust_id):
        url = 'https://public-api.secure.pixiv.net/v1/works/%d.json' % (illust_id)
        params = {
            'image_sizes': 'px_128x128,small,medium,large,px_480mw',
            'include_stats': 'true',
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 用户资料
    def users(self, author_id):
        url = 'https://public-api.secure.pixiv.net/v1/users/%d.json' % (author_id)
        params = {
            'profile_image_sizes': 'px_170x170,px_50x50',
            'image_sizes': 'px_128x128,small,medium,large,px_480mw',
            'include_stats': 1,
            'include_profile': 1,
            'include_workspace': 1,
            'include_contacts': 1,
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 我的订阅
    def me_feeds(self, show_r18=1, max_id=None):
        url = 'https://public-api.secure.pixiv.net/v1/me/feeds.json'
        params = {
            'relation': 'all',
            'type': 'touch_nottext',
            'show_r18': show_r18,
        }
        if max_id:
            params['max_id'] = max_id
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 获取收藏夹
    # publicity: public, private
    def me_favorite_works(self, page=1, per_page=50, publicity='public', image_sizes=['px_128x128', 'px_480mw', 'large']):
        url = 'https://public-api.secure.pixiv.net/v1/me/favorite_works.json'
        params = {
            'page': page,
            'per_page': per_page,
            'publicity': publicity,
            'image_sizes': ','.join(image_sizes),
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 添加收藏
    # publicity: public, private
    def me_favorite_works_add(self, work_id, publicity='public'):
        url = 'https://public-api.secure.pixiv.net/v1/me/favorite_works.json'
        params = {
            'work_id': work_id,
            'publicity': publicity,
        }
        r = self.auth_requests_call('POST', url, params=params)
        return self.parse_result(r)

    # 删除收藏
    # publicity: public, private
    def me_favorite_works_delete(self, ids, publicity='public'):
        url = 'https://public-api.secure.pixiv.net/v1/me/favorite_works.json'
        if isinstance(ids, list):
            params = {'ids': ",".join(map(str, ids)), 'publicity': publicity}
        else:
            params = {'ids': ids, 'publicity': publicity}
        r = self.auth_requests_call('DELETE', url, params=params)
        return self.parse_result(r)

    # 关注的新作品 (New -> Follow)
    def me_following_works(self, page=1, per_page=30,
                           image_sizes=['px_128x128', 'px_480mw', 'large'],
                           include_stats=True, include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/me/following/works.json'
        params = {
            'page': page,
            'per_page': per_page,
            'image_sizes': ','.join(image_sizes),
            'include_stats': include_stats,
            'include_sanity_level': include_sanity_level,
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 获取关注用户
    def me_following(self, page=1, per_page=30, publicity='public'):
        url = 'https://public-api.secure.pixiv.net/v1/me/following.json'
        params = {
            'page': page,
            'per_page': per_page,
            'publicity': publicity,
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 关注用户
    # publicity:  public, private
    def me_favorite_users_follow(self, user_id, publicity='public'):
        url = 'https://public-api.secure.pixiv.net/v1/me/favorite-users.json'
        params = {
            'target_user_id': user_id,
            'publicity': publicity
        }
        r = self.auth_requests_call('POST', url, params=params)
        return self.parse_result(r)

    # 解除关注用户
    def me_favorite_users_unfollow(self, user_ids, publicity='public'):
        url = 'https://public-api.secure.pixiv.net/v1/me/favorite-users.json'
        if type(user_ids) == list:
            params = {'delete_ids': ",".join(map(str, user_ids)), 'publicity': publicity}
        else:
            params = {'delete_ids': user_ids, 'publicity': publicity}
        r = self.auth_requests_call('DELETE', url, params=params)
        return self.parse_result(r)

    # 用户作品列表
    def users_works(self, author_id, page=1, per_page=30,
                    image_sizes=['px_128x128', 'px_480mw', 'large'],
                    include_stats=True, include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/users/%d/works.json' % (author_id)
        params = {
            'page': page,
            'per_page': per_page,
            'include_stats': include_stats,
            'include_sanity_level': include_sanity_level,
            'image_sizes': ','.join(image_sizes),
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 用户收藏
    def users_favorite_works(self, author_id, page=1, per_page=30,
                             image_sizes=['px_128x128', 'px_480mw', 'large'],
                             include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/users/%d/favorite_works.json' % (author_id)
        params = {
            'page': page,
            'per_page': per_page,
            'include_sanity_level': include_sanity_level,
            'image_sizes': ','.join(image_sizes),
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 用户活动
    def users_feeds(self, author_id, show_r18=1, max_id=None):
        url = 'https://public-api.secure.pixiv.net/v1/users/%d/feeds.json' % (author_id)
        params = {
            'relation': 'all',
            'type': 'touch_nottext',
            'show_r18': show_r18,
        }
        if max_id:
            params['max_id'] = max_id
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 用户关注的用户
    def users_following(self, author_id, page=1, per_page=30):
        url = 'https://public-api.secure.pixiv.net/v1/users/%d/following.json' % (author_id)
        params = {
            'page': page,
            'per_page': per_page,
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 排行榜/过去排行榜
    # ranking_type: [all, illust, manga, ugoira]
    # mode: [daily, weekly, monthly, rookie, original, male, female, daily_r18, weekly_r18, male_r18, female_r18, r18g]
    #       for 'illust' & 'manga': [daily, weekly, monthly, rookie, daily_r18, weekly_r18, r18g]
    #       for 'ugoira': [daily, weekly, daily_r18, weekly_r18],
    # page: [1-n]
    # date: '2015-04-01' (仅过去排行榜)
    def ranking(self, ranking_type='all', mode='daily', page=1, per_page=50, date=None,
                image_sizes=['px_128x128', 'px_480mw', 'large'],
                profile_image_sizes=['px_170x170', 'px_50x50'],
                include_stats=True, include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/ranking/%s.json' % (ranking_type)
        params = {
            'mode': mode,
            'page': page,
            'per_page': per_page,
            'include_stats': include_stats,
            'include_sanity_level': include_sanity_level,
            'image_sizes': ','.join(image_sizes),
            'profile_image_sizes': ','.join(profile_image_sizes),
        }
        if date:
            params['date'] = date
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # alias for old API ranking_all()
    def ranking_all(self, mode='daily', page=1, per_page=50, date=None,
                    image_sizes=['px_128x128', 'px_480mw', 'large'],
                    profile_image_sizes=['px_170x170', 'px_50x50'],
                    include_stats=True, include_sanity_level=True):
        return self.ranking(ranking_type='all', mode=mode, page=page, per_page=per_page, date=date,
                            image_sizes=image_sizes, profile_image_sizes=profile_image_sizes,
                            include_stats=include_stats, include_sanity_level=include_sanity_level)

    # 作品搜索
    def search_works(self, query, page=1, per_page=30, mode='text',
                     period='all', order='desc', sort='date',
                     types=['illustration', 'manga', 'ugoira'],
                     image_sizes=['px_128x128', 'px_480mw', 'large'],
                     include_stats=True, include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/search/works.json'
        params = {
            'q': query,
            'page': page,
            'per_page': per_page,
            'period': period,
            'order': order,
            'sort': sort,
            'mode': mode,
            'types': ','.join(types),
            'include_stats': include_stats,
            'include_sanity_level': include_sanity_level,
            'image_sizes': ','.join(image_sizes),
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

    # 最新作品 (New -> Everyone)
    def latest_works(self, page=1, per_page=30,
                     image_sizes=['px_128x128', 'px_480mw', 'large'],
                     profile_image_sizes=['px_170x170', 'px_50x50'],
                     include_stats=True, include_sanity_level=True):
        url = 'https://public-api.secure.pixiv.net/v1/works.json'
        params = {
            'page': page,
            'per_page': per_page,
            'include_stats': include_stats,
            'include_sanity_level': include_sanity_level,
            'image_sizes': ','.join(image_sizes),
            'profile_image_sizes': ','.join(profile_image_sizes),
        }
        r = self.auth_requests_call('GET', url, params=params)
        return self.parse_result(r)

# Experimental App-API (6.x - app-api.pixiv.net)
class AppPixivAPI(BasePixivAPI):
    """
    Warning: The AppPixivAPI backend is experimental !!!
    """

    def __init__(self, **requests_kwargs):
        """initialize requests kwargs if need be"""
        super(AppPixivAPI, self).__init__(**requests_kwargs)

    # Check auth and set BearerToken to headers
    def no_auth_requests_call(self, method, url, headers={}, params=None, data=None, req_auth=False):
        headers['App-OS'] = 'ios'
        headers['App-OS-Version'] = '9.3.3'
        headers['App-Version'] = '6.0.9'
        headers['User-Agent'] = 'PixivIOSApp/6.0.9 (iOS 9.3.3; iPhone8,1)'
        if (not req_auth):
            return self.requests_call(method, url, headers, params, data)
        else:
            self.require_auth()
            headers['Authorization'] = 'Bearer %s' % self.access_token
            return self.requests_call(method, url, headers, params, data)

    def parse_result(self, req):
        try:
            return self.parse_json(req.text)
        except Exception as e:
            raise PixivError("parse_json() error: %s" % (e), header=req.headers, body=req.text)

    def format_bool(self, bool_value):
        if type(bool_value) == bool:
            return 'true' if bool_value else 'false'
        if bool_value in ['true', 'True']:
            return 'true'
        else:
            return 'false'

    def parse_qs(self, next_url):
        if not next_url: return None
        if sys.version_info >= (3, 0):
            from urllib.parse import urlparse, parse_qs, unquote
            unquote_url = unquote(next_url)
        else:
            from urlparse import urlparse, parse_qs, unquote
            unquote_url = unquote(next_url.encode('utf8')).decode('utf8')
        query = urlparse(unquote_url).query
        return dict([(k,v[0]) for k,v in parse_qs(query).items()])

    # 用户详情 (无需登录)
    def user_detail(self, user_id, filter='for_ios', req_auth=False):
        url = 'https://app-api.pixiv.net/v1/user/detail'
        params = {
            'user_id': user_id,
            'filter': filter,
        }
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 用户作品列表 (无需登录)
    def user_illusts(self, user_id, type='illust', filter='for_ios', offset=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/user/illusts'
        params = {
            'user_id': user_id,
            'type': type,
            'filter': filter,
        }
        if (offset):
            params['offset'] = offset
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 用户收藏作品列表 (无需登录)
    def user_bookmarks_illust(self, user_id, restrict='public', filter='for_ios', max_bookmark_id=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/user/bookmarks/illust'
        params = {
            'user_id': user_id,
            'restrict': restrict,
            'filter': filter,
        }
        if (max_bookmark_id):
            params['max_bookmark_id'] = max_bookmark_id
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 关注用户的新作
    # restrict: [public, private]
    def illust_follow(self, restrict='public', offset=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v2/illust/follow'
        params = {
            'restrict': restrict,
        }
        if (offset):
            params['offset'] = offset
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 作品评论 (无需登录)
    def illust_comments(self, illust_id, offset=None, include_total_comments=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/illust/comments'
        params = {
            'illust_id': illust_id,
        }
        if (offset):
            params['offset'] = offset
        if (include_total_comments):
            params['include_total_comments'] = self.format_bool(include_total_comments)
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 相关作品列表 (无需登录)
    def illust_related(self, illust_id, filter='for_ios', seed_illust_ids=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/illust/related'
        params = {
            'illust_id': illust_id,
            'filter': filter,
        }
        if type(seed_illust_ids) == str:
            params['seed_illust_ids'] = seed_illust_ids
        if type(seed_illust_ids) == list:
            params['seed_illust_ids'] = ",".join([ str(iid) for iid in seed_illust_ids ])
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 插画推荐 (Home - Main) (无需登录)
    # content_type: [illust, manga]
    def illust_recommended(self, content_type='illust', include_ranking_label=True, filter='for_ios',
            max_bookmark_id_for_recommend=None, min_bookmark_id_for_recent_illust=None,
            offset=None, include_ranking=None, bookmark_illust_ids=None, req_auth=False):
        if (req_auth):
            url = 'https://app-api.pixiv.net/v1/illust/recommended'
        else:
            url = 'https://app-api.pixiv.net/v1/illust/recommended-nologin'
        params = {
            'content_type': content_type,
            'include_ranking_label': self.format_bool(include_ranking_label),
            'filter': filter,
        }
        if (max_bookmark_id_for_recommend):
            params['max_bookmark_id_for_recommend'] = max_bookmark_id_for_recommend
        if (min_bookmark_id_for_recent_illust):
            params['min_bookmark_id_for_recent_illust'] = min_bookmark_id_for_recent_illust
        if (offset):
            params['offset'] = offset
        if (include_ranking):
            params['include_ranking'] = self.format_bool(include_ranking)

        if (not req_auth):
            if (type(bookmark_illust_ids) == str):
                params['bookmark_illust_ids'] = bookmark_illust_ids
            if (type(bookmark_illust_ids) == list):
                params['bookmark_illust_ids'] = ",".join([ str(iid) for iid in bookmark_illust_ids ])

        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 作品排行
    # mode: [day, week, month, day_male, day_female, week_original, week_rookie, day_manga]
    # date: '2016-08-01'
    # mode (Past): [day, week, month, day_male, day_female, week_original, week_rookie,
    #               day_r18, day_male_r18, day_female_r18, week_r18, week_r18g]
    def illust_ranking(self, mode='day', filter='for_ios', date=None, offset=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/illust/ranking'
        params = {
            'mode': mode,
            'filter': filter,
        }
        if (date):
            params['date'] = date
        if (offset):
            params['offset'] = offset
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 趋势标签 (Search - tags) (无需登录)
    def trending_tags_illust(self, filter='for_ios', req_auth=False):
        url = 'https://app-api.pixiv.net/v1/trending-tags/illust'
        params = {
            'filter': filter,
        }
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

    # 搜索 (Search) (无需登录)
    # search_target - 搜索类型
    #   partial_match_for_tags  - 标签部分一致
    #   exact_match_for_tags    - 标签完全一致
    #   title_and_caption       - 标题说明文
    # sort: [date_desc, date_asc]
    # duration: [within_last_day, within_last_week, within_last_month]
    def search_illust(self, word, search_target='partial_match_for_tags', sort='date_desc', duration=None,
            filter='for_ios', offset=None, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/search/illust'
        params = {
            'word': word,
            'search_target': search_target,
            'sort': sort,
            'filter': filter,
        }
        if (duration):
            params['duration'] = duration
        if (offset):
            params['offset'] = offset
        r = self.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)
        return self.parse_result(r)

