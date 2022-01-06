'use strict';

const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

const port = 3000;
const catalogPath = path.resolve(__dirname, './data/showcase.json');
const cartPath = path.resolve(__dirname, './data/cart.json');
const staticDir = path.resolve(__dirname, './public/');

var cors = require('cors');

app.use(cors());
app.use(express.json());

app.use(express.static(staticDir));

app.get('/api/v1/showcase', (req, res) => {
    fs.readFile(catalogPath, 'utf-8', (err, data) => {
        if (!err) {
            res.send(data);
        } else {
            res.status(500).send(err)
        }
    })
})

app.get('/api/v1/cart', (req, res) => {
    fs.readFile(cartPath, 'utf-8', (err, data) => {
        if (!err) {

            res.send(data);
        } else {

            res.status(500).send(err)
        }
    })
})

app.post('/api/v1/cart', (req, res) => {
    const goodId = req.body.id_product;
    fs.readFile(catalogPath, 'utf-8', (err, data) => {
        if (!err) {
            const goods = JSON.parse(data);
            const good_idx = goods.findIndex(item =>
                item.id_product == goodId);
            const good_data = {
                id_product: goods[good_idx].id_product,
                price: goods[good_idx].price,
                product_name: goods[good_idx].product_name,
                quantity: 1
            };
            fs.readFile(cartPath, 'utf-8', (err, data) => {
                if (!err) {
                    const cart = JSON.parse(data);
                    const idx = cart.findIndex(stack =>
                        stack.id_product == good_data.id_product);
                    if (idx >= 0) {
                        cart[idx].quantity++;
                        cart[idx].price += good_data.price
                    } else {
                        cart.push(good_data);
                    }
                    fs.writeFile(cartPath, JSON.stringify(cart),
                        'utf-8', (err, data) => {
                            res.sendStatus(201);
                        })

                } else {
                    res.status(500).send(err);
                }
            })
        } else {
            res.status(500).send(err);
        }
    })
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})

app.post('/api/v1/cart/remove', (req, res) => {
    const goodId = req.body.id_product;
    fs.readFile(cartPath, 'utf-8', (err, data) => {
        if (!err) {
            const cart = JSON.parse(data);
            const idx = cart.findIndex(stack => stack.id_product == goodId)
            if (idx >= 0) {
                const goodPrice = cart[idx].price / cart[idx].quantity
                --cart[idx].quantity;
                cart[idx].price -= goodPrice;
                if (cart[idx].quantity == 0) {
                    cart.splice(idx, 1);
                }
                fs.writeFile(cartPath, JSON.stringify(cart), 'utf-8',
                    (err, data) => {
                        res.sendStatus(201)
                    })
            } else {
                res.sendStatus(201)
            }
        } else {
            res.status(500).send(err);
        }
    })
})
