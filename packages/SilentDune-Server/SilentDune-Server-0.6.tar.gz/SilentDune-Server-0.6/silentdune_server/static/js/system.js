/*
#
# Authors: Robert Abram <robert.abram@entpack.com>
#
# Copyright (C) 2015 EntPack
# see file 'LICENSE' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function silentdune_system () {

    // Set default environment id+values here
    this.env = {
        request_timeout: 180
    };

    /* Store id + value pairs, p can be an array. IE: set_env({ 'id1': 'test', 'id2': 2, 'ed3': true } */
    this.set_env = function (p, value) {
        if (p != null && typeof p === 'object' && !value) for (var n in p) this.env[n] = p[n];
         else this.env[p] = value
    };


    this.unload = false;

    /* Get the csrf token */
    this.set_env({'csrftoken': Cookies.get('csrftoken') });

    $.ajaxSetup({
        cache: false,
        timeout: this.env.request_timeout * 1000,
        error: function (request, status, err) {
            this.http_error(request, status, err)
        },
        beforeSend: function (xmlhttp, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xmlhttp.setRequestHeader('X-CSRFToken', this.env.csrftoken)
            }
        }
    });

    /* figure out if the window is closing */
    $(window).bind('beforeunload', function () {
        this.unload = true
    });

    this.init = function () {

        switch (this.env.app) {
            case 'dashboard': {

            }
        }


    };


    this.lock_form = function (form, lock) {
        if (!form || !form.elements) return ;
        var n,
        len,
        elm;
        if (lock) this.disabled_form_elements = [
        ];
        for (n = 0, len = form.elements.length; n < len; n++) {
            elm = form.elements[n];
            if (elm.type == 'hidden') continue;
            if (lock && elm.disabled) this.disabled_form_elements.push(elm);
             else if (lock || $.inArray(elm, this.disabled_form_elements) < 0) elm.disabled = lock
        }
    };




}