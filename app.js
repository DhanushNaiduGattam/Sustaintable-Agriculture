// Handle prediction form
document.getElementById("predictForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  // Convert numbers properly
  data.min_price = parseFloat(data.min_price);
  data.max_price = parseFloat(data.max_price);

  const res = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("msg").textContent =
    result.predicted_modal_price
      ? `Predicted Modal Price: ${result.predicted_modal_price}`
      : `Error: ${result.error}`;
});

// Load CSV data into table
async function loadData() {
  const res = await fetch("http://127.0.0.1:8000/data");
  const data = await res.json();

  const tbody = document.querySelector("#dataTable tbody");
  tbody.innerHTML = "";

  data.forEach(row => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${row.state}</td>
      <td>${row.district}</td>
      <td>${row.market}</td>
      <td>${row.commodity}</td>
      <td>${row.variety}</td>
      <td>${row.min_price}</td>
      <td>${row.max_price}</td>
      <td>${row.modal_price}</td>
    `;
    tbody.appendChild(tr);
  });
}
