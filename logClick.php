<?php


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $page = $_POST['page'];

    $file = fopen('click_data.csv', 'a');

    fputcsv($file, array($page));

    fclose($file);

    http_response_code(200);
    echo "Click data logged successfully";
} else {
    // If the request method is not POST, return a 405 Method Not Allowed error
    http_response_code(405);
    echo "Method Not Allowed";
}
