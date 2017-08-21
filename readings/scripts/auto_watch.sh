for i in 10 {12..14} {16..25} {30..37} {47..48} {50..53} {150..175} 200 201; do
    
    echo "192.168.254.$i"; 
    
done | xargs -P0 -I {}  bash ipmi_run_backup.sh {}
