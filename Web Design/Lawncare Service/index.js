// -------------------------------------------------------------
// Mo's Lawncare Services
// Author: Logan Marsh
// Date: November 19th 2025
// Description:
//     Calculates border trimming, lawn mowing, fertilizer,
//     HST, environmental tax, and displays results in a table.
// -------------------------------------------------------------

// Quick function to get element by ID
var $ = function (id) {
  return document.getElementById(id);
};

// -------------------------------------------------------------
// Formatted printing objects already provided
// -------------------------------------------------------------
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// -------------------------------------------------------------
// PROGRAM CONSTANTS
// -------------------------------------------------------------
const BORDER_PERCENT = 0.04;   // 4% of total area
const BORDER_RATE = 0.28;      // $0.28 per sq ft

const MOW_PERCENT = 0.96;      // remaining 96% of area
const MOW_RATE = 0.04;         // $0.04 per sq ft

const FERT_RATE = 0.03;        // $0.03 per sq ft

const HST_RATE = 0.15;         // 15% sales tax
const ENV_RATE = 0.014;        // 1.4% environmental tax

// -------------------------------------------------------------
// formatMoney() — wrapper for readability
// -------------------------------------------------------------
function formatMoney(num) {
  return cur2Format.format(num);
}

// -------------------------------------------------------------
// Main Function – Runs when button clicked
// -------------------------------------------------------------
function generateInvoice() {

  // ---------------- INPUT RETRIEVAL -------------------------
  let name = $("custName").value.trim();
  let street = $("custStreet").value.trim();
  let city = $("custCity").value.trim();
  let phone = $("custPhone").value.trim();
  let sqFeet = $("sqFeet").value.trim();

  // ---------------- INPUT VALIDATION ------------------------
  if (name === "" || street === "" || city === "") {
    alert("Please complete all customer details.");
    return;
  }

  if (!/^\d{3}-\d{3}-\d{4}$/.test(phone)) {
    alert("Phone number must be in the format 999-999-9999.");
    return;
  }

  if (!/^\d+$/.test(sqFeet)) {
    alert("Total square feet must be a number.");
    return;
  }

  sqFeet = parseFloat(sqFeet);

  // ------------------- CALCULATIONS -------------------------

  // Border trimming
  let borderArea = sqFeet * BORDER_PERCENT;
  let borderCost = borderArea * BORDER_RATE;

  // Lawn mowing
  let mowArea = sqFeet * MOW_PERCENT;
  let mowCost = mowArea * MOW_RATE;

  // Fertilizer
  let fertCost = sqFeet * FERT_RATE;

  // Total before tax
  let totalCharges = borderCost + mowCost + fertCost;

  // Taxes
  let hst = totalCharges * HST_RATE;
  let envTax = totalCharges * ENV_RATE;

  // Invoice total
  let invoiceTotal = totalCharges + hst + envTax;

  // ------------------- CUSTOMER BLOCK -----------------------
  let customerBlock = `
        <strong>${name}</strong><br>
        ${street}<br>
        ${city} &nbsp;&nbsp; ${phone}
    `;

  // ------------------- OUTPUT TABLE -------------------------
  $("output").innerHTML = `
      <h2>Service Invoice</h2>
      <p>${customerBlock}</p>

      <table class="resultTable">
        <tr>
          <th>Description</th>
          <th>Amount</th>
        </tr>

        <tr>
          <td>Border Trimming</td>
          <td class="amt">${formatMoney(borderCost)}</td>
        </tr>

        <tr>
          <td>Lawn Mowing</td>
          <td class="amt">${formatMoney(mowCost)}</td>
        </tr>

        <tr>
          <td>Fertilizer Treatment</td>
          <td class="amt">${formatMoney(fertCost)}</td>
        </tr>

        <tr>
          <td><strong>Total Charges</strong></td>
          <td class="amt"><strong>${formatMoney(totalCharges)}</strong></td>
        </tr>

        <tr>
          <td>HST (15%)</td>
          <td class="amt">${formatMoney(hst)}</td>
        </tr>

        <tr>
          <td>Environmental Tax (1.4%)</td>
          <td class="amt">${formatMoney(envTax)}</td>
        </tr>

        <tr>
          <td><strong>Invoice Total</strong></td>
          <td class="amt"><strong>${formatMoney(invoiceTotal)}</strong></td>
        </tr>
      </table>
    `;
}

// -------------------------------------------------------------
// EVENT LISTENER
// -------------------------------------------------------------
$("btnCalc").addEventListener("click", generateInvoice);
