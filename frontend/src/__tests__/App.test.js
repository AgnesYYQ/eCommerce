import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders navigation links', () => {
  render(<App />);
  expect(screen.getByText(/Home/i)).toBeInTheDocument();
  expect(screen.getByText(/Products/i)).toBeInTheDocument();
});
