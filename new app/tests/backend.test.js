const request = require('supertest');
const app = require('../app'); // Assuming app.js is the entry point

describe('Expense Tracker API Tests', () => {
    test('GET /expenses should return all expenses', async () => {
        const response = await request(app).get('/expenses');
        expect(response.status).toBe(200);
        expect(Array.isArray(response.body)).toBe(true);
    });

    test('POST /expenses should create a new expense', async () => {
        const newExpense = { category: 'Food', amount: 50, description: 'Lunch' };
        const response = await request(app).post('/expenses').send(newExpense);
        expect(response.status).toBe(201);
        expect(response.body).toMatchObject(newExpense);
    });

    // ...additional tests...
});
