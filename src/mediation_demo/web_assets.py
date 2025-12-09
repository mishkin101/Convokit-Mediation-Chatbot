HTML_web ="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Order Confirmation</title>
  <style>
    :root {
      --primary: #4838F5;
      --sidebar-bg: #DFC271;
      --card-gray: #f1f1f1;
      --text-dark: #151515;
      --accent-green: #c9f5c9;
      --border-radius-lg: 18px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: #151515;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text-dark);
    }

    .app {
      max-width: 1280px;
      margin: 24px auto;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
    }

    /* TOP NAVBAR -------------------------------------------------------- */

    .topnav {
      background: var(--primary);
      color: #ffffff;
      display: flex;
      align-items: center;
      padding: 0 48px;
      height: 72px;
    }

    .logo {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: 3px solid #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      margin-right: 56px;
    }

    .logo span {
      font-size: 18px;
    }

    .nav-links {
      display: flex;
      gap: 56px;
      font-size: 18px;
      letter-spacing: 0.12em;
    }

    .nav-link {
      position: relative;
      cursor: pointer;
      opacity: 0.9;
    }

    .nav-link:hover {
      opacity: 1;
    }

    .nav-link.active::after {
      content: "";
      position: absolute;
      left: 0;
      right: 0;
      bottom: -10px;
      margin: 0 auto;
      width: 70%;
      height: 3px;
      border-radius: 999px;
      background: #ffffff;
    }

    /* LAYOUT ------------------------------------------------------------ */

    .content {
      display: flex;
      min-height: 640px;
    }

  

    .sidebar {
      width: 230px;
      background: var(--sidebar-bg);
      padding: 32px 24px;
    }

    .user-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 32px;
    }

    .avatar {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 2px solid #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }

    .user-name {
      font-weight: 600;
      font-size: 16px;
    }

    .sidebar-nav {
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 14px;
    }

    .sidebar-link {
      cursor: pointer;
      color: #fffef5;
      opacity: 0.9;
    }

    .sidebar-link:hover {
      opacity: 1;
      text-decoration: underline;
    }

    .sidebar-link.logout {
      margin-top: 24px;
      font-weight: 600;
    }

    /* MAIN AREA --------------------------------------------------------- */

    .main {
      flex: 1;
      padding: 32px 40px 40px 40px;
      display: flex;
      flex-direction: column;
      gap: 26px;
    }

    .thankyou-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }

    .thankyou-text h1 {
      font-size: 32px;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }

    .thankyou-text h1 span {
      display: block;
    }

    .order-id {
      font-weight: 600;
      font-size: 18px;
    }

    .status-pill {
      padding: 8px 26px;
      border-radius: 999px;
      background: var(--accent-green);
      font-size: 12px;
      font-weight: 500;
      color: #3f7c3f;
    }

    .upper-row {
      display: grid;
      grid-template-columns: 220px minmax(260px, 1.2fr) 280px;
      gap: 32px;
      align-items: flex-start;
    }

    /* PRODUCT PANEL */

    .product-panel {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }

    .product-image {
      width: 190px;
      height: 220px;
      border-radius: 10px;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffd54a;
      font-weight: 700;
      text-align: center;
    }

    .product-image span {
      font-size: 22px;
    }

    /* ORDER DETAILS ----------------------------------------------------- */

    .order-details {
      font-size: 14px;
    }

    .price-header {
      display: grid;
      grid-template-columns: 1fr 0.5fr 0.8fr;
      font-weight: 600;
      border-bottom: 1px solid #ccc;
      padding-bottom: 4px;
      margin-bottom: 6px;
    }

    .price-row {
      display: grid;
      grid-template-columns: 1fr 0.5fr 0.8fr;
      padding: 4px 0 10px;
    }

    .ship-to {
      margin-top: 12px;
      font-size: 13px;
    }

    .ship-to-title {
      font-weight: 600;
      margin-bottom: 4px;
    }

    /* RIGHT CARDS ------------------------------------------------------- */

    .right-cards {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .card {
      background: var(--card-gray);
      border-radius: var(--border-radius-lg);
      padding: 18px 20px;
      font-size: 13px;
    }

    .card-title {
      font-weight: 600;
      margin-bottom: 6px;
    }

    .card-subtext {
      font-size: 12px;
      margin-bottom: 14px;
    }

    .pill-button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      padding: 8px 18px;
      background: #ffffff;
      color: var(--primary);
      font-size: 12px;
      font-weight: 600;
      border: none;
      cursor: pointer;
      margin-bottom: 10px;
    }

    .pill-button.chat {
      background: var(--primary);
      color: #ffffff;
      margin-top: 12px;
    }

    .card-footer {
      margin-top: 8px;
      font-size: 11px;
      color: #555;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .small-icon {
      font-size: 14px;
    }

    .card-center {
      text-align: center;
    }

    .card-center .card-title {
      font-size: 16px;
      margin-bottom: 6px;
    }

    /* ORDER SUMMARY ----------------------------------------------------- */

    .summary-card {
      margin-top: 8px;
      background: var(--card-gray);
      border-radius: var(--border-radius-lg);
      padding: 18px 26px;
      font-size: 14px;
    }

    .summary-title {
      font-weight: 600;
      margin-bottom: 10px;
    }

    .summary-row {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      padding: 4px 0;
      color: #555;
    }

    .summary-row.header {
      font-weight: 600;
      color: #777;
    }

    .summary-row.total {
      margin-top: 8px;
      font-weight: 700;
      color: #000;
    }
  </style>
</head>
<body>
  <div class="app">
    <!-- TOP NAV -->
    <header class="topnav">
      <div class="logo">
        <span>🏀</span>
      </div>
      <nav class="nav-links">
        <div class="nav-link">Featured</div>
        <div class="nav-link">Products</div>
        <div class="nav-link">About</div>
        <div class="nav-link">Contact Us</div>
        <div class="nav-link active">Profile</div>
      </nav>
    </header>

    <div class="content">
      <!-- SIDEBAR -->
      <aside class="sidebar">
        <div class="user-header">
          <div class="avatar">☺</div>
          <div class="user-name">John B.</div>
        </div>
        <nav class="sidebar-nav">
          <div class="sidebar-link">Personal Information</div>
          <div class="sidebar-link">Addresses</div>
          <div class="sidebar-link">Wishlist</div>
          <div class="sidebar-link">My Orders</div>
          <div class="sidebar-link">My Order Details</div>
          <div class="sidebar-link logout">Logout</div>
        </nav>
      </aside>

      <!-- MAIN CONTENT -->
      <main class="main">
        <div class="thankyou-row">
          <div class="thankyou-text">
            <h1>
              <span>THANK YOU,</span>
              <span>JOHN!</span>
            </h1>
            <div class="order-id">Order ID: 2637839300</div>
          </div>
          <div class="status-pill">Delivered</div>
        </div>

        <div class="upper-row">
          <!-- Product -->
          <section class="product-panel">
            <div class="product-image">
              <span>BRYANT<br />24</span>
            </div>
          </section>

          <!-- Order details -->
          <section class="order-details">
            <div class="price-header">
              <div>Price</div>
              <div>QTY</div>
              <div>AMOUNT</div>
            </div>
            <div class="price-row">
              <div>$24.99</div>
              <div>1</div>
              <div>$24.99</div>
            </div>

            <div class="ship-to">
              <div class="ship-to-title">Ship to:</div>
              <div>2514 Ocean Avenue</div>
              <div>Los Angeles, CA, 98132</div>
              <div>US</div>
            </div>
          </section>

          <!-- Right cards -->
          <section class="right-cards">
            <div class="card">
              <div class="card-title">Like what you got? We would love to know!</div>
              <div class="card-subtext"></div>
              <button class="pill-button">⭐ Rate and Review</button>
              <div class="card-footer">
                <span class="small-icon">ⓘ</span>
                <span>Return policy: active until Dec 15th</span>
              </div>
            </div>

            <div class="card card-center">
              <div class="small-icon" style="font-size:24px;">💬</div>
              <div class="card-title">Need Help?</div>
              <div class="card-subtext">
                Do you have any questions or concerns with your order?<br />
                We are more than happy to assist you.
              </div>
              <button class="pill-button chat">Chat with us</button>
            </div>
          </section>
        </div>

        <!-- Order summary -->
        <section class="summary-card">
          <div class="summary-title">Order Summary</div>

          <div class="summary-row header">
            <div></div>
            <div></div>
            <div></div>
          </div>

          <div class="summary-row">
            <div>Subtotal</div>
            <div></div>
            <div>$24.99</div>
          </div>
          <div class="summary-row">
            <div>Discount</div>
            <div>$0.00</div>
            <div>-$1.00</div>
          </div>
          <div class="summary-row">
            <div>Shipping</div>
            <div>Free Shipping</div>
            <div>$0.00</div>
          </div>
          <div class="summary-row">
            <div>Tax</div>
            <div>$0.87</div>
            <div>$0.87</div>
          </div>

          <div class="summary-row total">
            <div>Total</div>
            <div></div>
            <div>$25.86</div>
          </div>
        </section>
      </main>
    </div>
  </div>
</body>
</html>
"""
