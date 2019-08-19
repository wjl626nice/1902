import $ from 'jquery'
import './css/1.css'

$(function() {
    $('li:odd').css('backgroundColor', 'green');
    $('li:even').css('backgroundColor', 'pink');
});
class Person {
    static a = 11
}
console.log(Person.a)

import Vue from 'vue'
import App from './components/App.vue'

const vm = new Vue({
    el: '#app',
    render: h => h(App)
})