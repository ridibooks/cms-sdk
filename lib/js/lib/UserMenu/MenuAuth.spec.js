import 'babel-polyfill';
import MenuAuth from './MenuAuth';
import { expect } from 'chai';

describe('MenuAuth', function () {
    it('tests if MenuAuth includes test url', function () {
        const userMenu = {
            'auths': [
                { id: 9,
                    menu_url: '/super/logs',
                    menu_deep: 1,
                    is_use: true,
                    is_show: true,
                    ajax_array: [],
                    auth: [] }
            ]
        };
        const testUrl = '/super/logs';
        expect(MenuAuth(userMenu, '', testUrl)).to.equal(true);
    });
});