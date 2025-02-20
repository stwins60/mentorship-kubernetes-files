require('dotenv').config();  
const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;
const FLASK_API_URL = process.env.FLASK_API_URL || 'http://localhost:5000/api/products';

app.get('/', async (req, res) => {
    try {
        const response = await axios.get(FLASK_API_URL);
        let productList = response.data.map(product =>
            `<li>${product.name} - $${product.price} (${product.category})</li>`).join('');
        res.send(`<h1>Product List</h1><ul>${productList}</ul>`);
    } catch (error) {
        res.send('<h1>Error fetching products from Flask API</h1>');
    }
});

app.listen(PORT, () => {
    console.log(`Node.js server running on http://localhost:${PORT}`);
});
