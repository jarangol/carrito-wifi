<?php
$valor_estado=$_POST['valor_estado'];
switch ($valor_estado) {
	case 1:
		exec('sudo python /var/www/html/carrito-wifi/py/avanza.py');
		break;
	case 2:
		exec('sudo python /var/www/html/carrito-wifi/py/izquierda.py');
		break;
	case 3:
		exec('sudo python /var/www/html//carrito-wifi/py/derecha.py');
		break;
	case 4:
		exec('sudo python /var/www/html/carrito-wifi/py/retrocede.py');
		break;
	case 5:
		exec('sudo python /var/www/html/carrito-wifi/py/para.py');
		break;
	default:
		exec('sudo python /var/www/html/carrito-wifi/py/para.py');
		break;
}
?>
