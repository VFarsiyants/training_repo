'use strict';
const goods = [
    { title: 'Shirt', price: 150 },
    { title: 'Socs', price: 50 },
    { title: 'Jacket', price: 350 },
    { title: 'Shoes', price: 250 },
];

// поскольку у нас цельное выражение return можно опустить фигурные скобки и 
// убрать return

// добавлены значения по умолячанию для переменных функции title
const renderGoodsItem = (title = 'without title', price = 'without price') =>
    `<div class="goods-item"><div class="goods-item-image"></div><h3>${title}</h3><p>${price}$</p></div>`;

// поскольку у нас одна переменная можем убрать курглые скобки при задании
// переменных стрелочной функции
const renderGoodsList = list => {
    let goodsList = list.map(item => renderGoodsItem(item.title, item.price));
    // чтобы убрать запятые необходимо в join определить в качестве сепаратора 
    // пустую строку
    document.querySelector('.goods-list').innerHTML = goodsList.join('');
};

renderGoodsList(goods);
