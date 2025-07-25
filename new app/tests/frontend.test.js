import { render, screen } from '@testing-library/react';
import ExpenseTracker from '../components/ExpenseTracker';

describe('Expense Tracker Component Tests', () => {
    test('renders the expense tracker header', () => {
        render(<ExpenseTracker />);
        const headerElement = screen.getByText(/Expense Tracker/i);
        expect(headerElement).toBeInTheDocument();
    });

    test('displays the add expense button', () => {
        render(<ExpenseTracker />);
        const buttonElement = screen.getByText(/Add Expense/i);
        expect(buttonElement).toBeInTheDocument();
    });

    // ...additional tests...
});
