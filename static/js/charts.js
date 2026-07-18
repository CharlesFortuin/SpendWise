const labels = expenses.map(expense => expense.category);

const data = expenses.map(expense => expense.total);

const ctx = document.getElementById("expenseChart");

new Chart(ctx, {
    type: "pie",
    data: {
        labels: labels,
        datasets: [{
            label: "Expenses",
            data: data,
            backgroundColor: [
                "#3498db",
                "#2ecc71",
                "#f39c12",
                "#e74c3c",
                "#9b59b6",
                "#1abc9c",
                "#34495e"
            ] 
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "bottom"
            }
        }
    }
});