import { render, screen } from '@testing-library/react';
import ProductList from '../pages/ProductList';

test('renders product list', () => {
  render(<ProductList />);
  expect(screen.getByText(/Product A/i)).toBeInTheDocument();
  expect(screen.getByText(/Product B/i)).toBeInTheDocument();
  expect(screen.getByText(/Product C/i)).toBeInTheDocument();
});
