// 定义模块的私有成员
let a = 10;
let c = 20;
// 定义一个外部访问不到的变量，不暴露
let d = 30;

function show() {

}
// 将本模块的私有成员暴露出去，供其他模块使用
export default {
    a,
    c,
    show
}
// export default {
//     d
// }

export let s1 = 'aaaa';
export let s2 = 'bbbb';
export function walk() {
    console.log('你会走！');
}