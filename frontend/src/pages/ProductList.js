import React from "react";

const mockProducts = [
  { id: 1, name: "Product A", description: "Description for product A", price: 19.99 },
  { id: 2, name: "Product B", description: "Description for product B", price: 29.99 },
  { id: 3, name: "Product C", description: "Description for product C", price: 39.99 },
];

export default function ProductList() {
  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {mockProducts.map((product) => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>Price: ${product.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
