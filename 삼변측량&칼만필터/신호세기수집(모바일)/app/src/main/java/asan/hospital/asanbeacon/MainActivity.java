package asan.hospital.asanbeacon;

import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.content.SharedPreferences;
import android.databinding.DataBindingUtil;
import android.net.Uri;
import android.os.Bundle;
import android.os.Message;
import android.os.RemoteException;
import android.os.StrictMode;
import android.support.v7.widget.LinearLayoutManager;
import android.util.Log;
import android.view.View;
import android.os.Handler;
import android.widget.Button;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

import org.altbeacon.beacon.Beacon;
import org.altbeacon.beacon.BeaconConsumer;
import org.altbeacon.beacon.BeaconManager;
import org.altbeacon.beacon.BeaconParser;
import org.altbeacon.beacon.MonitorNotifier;
import org.altbeacon.beacon.RangeNotifier;
import org.altbeacon.beacon.Region;
import org.altbeacon.beacon.distance.AndroidModel;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.text.DecimalFormat;
import java.util.Collection;
import java.util.Iterator;
import java.util.Vector;


import asan.hospital.asanbeacon.databinding.ActivityMainBinding;

public class MainActivity extends BaseActivity implements BeaconConsumer {
    private String return_msg;
    int x_1 = 6;
    int y_1 = 6;
    int x_2 = 0;
    int y_2 = 6;
    int x_3 = 0;
    int y_3 = 0;
    double R_1 = 0;
    double R_2 = 0;
    double R_3 = 0;
    int a,b,c;
    double D1,D2,D3;
    String location;
    /*int beacon_1 = 0;
    int beacon_2 = 0;
    int beacon_3 = 0;*/


    private static final String BEACON_PARSER = "m:2-3=0215,i:4-19,i:20-21,i:22-23,p:24-24,d:25-25";

    private DecimalFormat decimalFormat = new DecimalFormat("#.##");

    private static final String TAG = "MainActivity";

    private static final int REQUEST_ENABLE_BT = 100;

    BluetoothAdapter mBluetoothAdapter;

    BeaconAdapter beaconAdapter;

    ActivityMainBinding binding;

    BeaconManager mBeaconManager;

    Vector<Item> items;

    LinearLayoutManager manager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);

        String url = "http://192.168.1.4:8080/ELL.html";
        final WebView webView = (WebView)findViewById(R.id.webview);
        webView.setWebViewClient(new WebViewClient());
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webView.loadUrl(url);

        Button reload_Button = (Button)findViewById(R.id.reload);
        reload_Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                webView.reload();
            }
        });

        AndroidModel am = AndroidModel.forThisDevice();
        Log.d("getManufacturer()",am.getManufacturer());
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        if (!mBluetoothAdapter.isEnabled()) {
            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);

            startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
        } else {
            mBeaconManager = BeaconManager.getInstanceForApplication(this);
            mBeaconManager.getBeaconParsers().add(new BeaconParser().setBeaconLayout(BEACON_PARSER));
            //BeaconManager.setRssiFilterImplClass(ArmaRssiFilter.class);
        }
        Button button1 = (Button) findViewById(R.id.phto);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://192.168.43.196:3000"));
                startActivity(intent);
            }
        });

        binding.scanBleFAB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (mBeaconManager.isBound(MainActivity.this)) {
                    binding.scanBleFAB.setImageResource(R.drawable.ic_visibility_white_24dp);
                    Log.i(TAG, "Stop BLE Scanning...");
                    mBeaconManager.unbind(MainActivity.this);
                } else {
                    binding.scanBleFAB.setImageResource(R.drawable.ic_visibility_off_white_24dp);
                    Log.i(TAG, "Start BLE Scanning...");
                    mBeaconManager.bind(MainActivity.this);
                }
            }
        });
        manager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        binding.beaconListView.setLayoutManager(manager);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        mBeaconManager.unbind(this);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_ENABLE_BT) {
            mBeaconManager = BeaconManager.getInstanceForApplication(this);
            mBeaconManager.getBeaconParsers().add(new BeaconParser().setBeaconLayout(BEACON_PARSER));
            //BeaconManager.setRssiFilterImplClass(ArmaRssiFilter.class);
        }

    }
    protected void List_save(int minor, double distance)
    {
        if (minor == 17952) {
            D1=distance;
            a = 1;
        }
        else if (minor == 13453){
            D2=distance;
            b = 1;
        }
        else if (minor == 18479){
            D3=distance;
            c = 1;
        }

        if(a == 1 && b == 1 && c ==1)
        {
            Calculate(D1,D2,D3);
            a = 0;
            b = 0;
            c = 0;
        }
    }

    protected void Calculate(double R_1,double R_2, double R_3)
    {

      /*  R_1 = Math.pow(10,((-59-R_1)/20));
        R_2 = Math.pow(10,((-59-R_2)/20));
        R_3 = Math.pow(10,((-59-R_3)/20));*/
        String Distanse_1 = String.valueOf(R_1);
        String Distanse_2 = String.valueOf(R_2);
        String Distanse_3 = String.valueOf(R_3);

        Distanse_1 = String.format("%.2f",R_1);
        Distanse_2 = String.format("%.2f",R_2);
        Distanse_3 = String.format("%.2f",R_3);
       
        location = Distanse_1+","+Distanse_2+","+Distanse_3;
        TCPclient tcpThread = new TCPclient(location);
        Thread thread = new Thread(tcpThread);
        thread.start();
    }
    /*protected void classfy(int minor,double rssi) {
        if (beacon_1 < 0 ) {
            beacon_1 = minor;
            R_1 = rssi;
        }
        else{
            if (beacon_2 < 0 && beacon_1 != minor){
                beacon_2 = minor;
                R_2 = rssi;
            }
            else{
                if (beacon_3 < 0 && beacon_1 != minor && beacon_2 != minor){
                    beacon_3 = minor;
                    R_3 = rssi;
                }
                else{
                    Calculate(R_1,R_2,R_3);
                    R_1 = 0;
                    R_2 = 0;
                    R_3 = 0;
                    beacon_1 = 0;
                    beacon_2 = 0;
                    beacon_3 = 0;
                }

            }
        }

       /* if (minor == 17952) {
            R_1 = rssi;
            List_save(minor, R_1);
        }
        else if (minor == 13453){
            R_2 = rssi;
            List_save(minor, R_2);
        }
        else if (minor == 18479){
            R_3 = rssi;
            List_save(minor, R_3);
        }
    }*/
    private class TCPclient implements Runnable {

        private static final String serverIP = "192.168.1.4";

        private static final int serverPort = 4000;

        private Socket inetSocket = null;

        private String msg;
        //private String return_msg;
        public TCPclient(String _msg) {
            this.msg = _msg;
        }
        public void run() {

            // TODO Auto-generated method stub

            try {

                Log.d("TCP", "C: Connecting...");

                inetSocket = new Socket(serverIP, serverPort);

                //inetSocket.connect(socketAddr);

                try {

                    Log.d("TCP", "C: Sending: '" + msg + "'");

                    PrintWriter out = new PrintWriter(new BufferedWriter(

                            new OutputStreamWriter(inetSocket.getOutputStream())), true);

                    out.println(msg);



                    BufferedReader in = new BufferedReader(

                            new InputStreamReader(inetSocket.getInputStream()));

                    return_msg = in.readLine();

                    Log.d("TCP", "C: Server send to me this message -->" + return_msg);

                } catch (Exception e) {

                    Log.e("TCP", "C: Error1", e);

                } finally {

                    inetSocket.close();

                }

            } catch (Exception e) {

                Log.e("TCP", "C: Error2", e);

            }
        }

    }
    @Override
    public void onBeaconServiceConnect() {
        mBeaconManager.addRangeNotifier(new RangeNotifier()
        {
            int beacon_1 = -1;
            int beacon_2 = -1;
            int beacon_3 = -1;
            @Override
            public void didRangeBeaconsInRegion(Collection<Beacon> beacons, Region region) {
                if (beacons.size() > 0) {
                    Iterator<Beacon> iterator = beacons.iterator();
                    items = new Vector<>();
                    while (iterator.hasNext()) {
                        Beacon beacon = iterator.next();
                        String address = beacon.getBluetoothAddress();
                            double rssi = beacon.getRssi();
                            int txPower = beacon.getTxPower();
                            double distance = Double.parseDouble(decimalFormat.format(beacon.getDistance()));
                            int major = beacon.getId2().toInt();
                            int minor = beacon.getId3().toInt();
                        if (beacon_1 < 0 ) {
                            beacon_1 = minor;
                            R_1 = rssi;
                        }
                        else{
                            if (beacon_2 < 0 && beacon_1 != minor){
                                beacon_2 = minor;
                                R_2 = rssi;
                            }
                            else{
                                if (beacon_3 < 0 && beacon_1 != minor && beacon_2 != minor){
                                    beacon_3 = minor;
                                    R_3 = rssi;
                                }
                                else{
                                    Calculate(R_1,R_2,R_3);
                                    R_1 = 0;
                                    R_2 = 0;
                                    R_3 = 0;
                                    beacon_1 = -1;
                                    beacon_2 = -1;
                                    beacon_3 = -1;
                                }

                            }
                        }
                            //classfy(minor,distance);
                            items.add(new Item(address, rssi, txPower, distance, major, minor));
                    }
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            beaconAdapter = new BeaconAdapter(items, MainActivity.this);
                            binding.beaconListView.setAdapter(beaconAdapter);
                            beaconAdapter.notifyDataSetChanged();
                        }
                    });
                }
            }
        });
        try {
            mBeaconManager.startRangingBeaconsInRegion(new Region("myRangingUniqueId", null, null, null));
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        mBeaconManager.addMonitorNotifier(new MonitorNotifier() {

            @Override
            public void didEnterRegion(Region region) {
                Log.i(TAG, "I just saw an beacon for the first time!");
            }

            @Override
            public void didExitRegion(Region region) {
                Log.i(TAG, "I no longer see an beacon");
            }


            @Override
            public void didDetermineStateForRegion(int state, Region region) {
                    Log.i(TAG, "I have just switched from seeing/not seeing beacons: "+state);
            }
        });
        try {
            mBeaconManager.startMonitoringBeaconsInRegion(new Region("myMonitoringUniqueId", null, null, null));
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }
}
