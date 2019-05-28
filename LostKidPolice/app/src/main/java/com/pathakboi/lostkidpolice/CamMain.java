package com.pathakboi.lostkidpolice;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

public class CamMain extends AppCompatActivity {
    ImageView imageView;
    EditText address;
    EditText number;
    Button submit;
    LocationManager locationManager;
    LocationListener locationListener;
    Double longitude, latitude;

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED){
            if(ContextCompat.checkSelfPermission(this,Manifest.permission.ACCESS_FINE_LOCATION)== PackageManager.PERMISSION_GRANTED){
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,30000,5, locationListener);
            }
        }
    }
    public void updateLocationInfo(Location location){
        longitude = location.getLongitude();
        latitude = location.getLatitude();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cam_main);

        Bundle extras = getIntent().getExtras();
        final byte[] byteArray = extras.getByteArray("picture");
        final Bitmap bmp = BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);

        imageView = (ImageView) findViewById(R.id.imageView1);
        imageView.setImageBitmap(bmp);
        address = (EditText) findViewById(R.id.textView5);
        number = (EditText) findViewById(R.id.editText2);
        submit = (Button) findViewById(R.id.button2);


        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
        locationListener = new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                updateLocationInfo(location);
            }
            @Override
            public void onStatusChanged(String s, int i, Bundle bundle) {}
            @Override
            public void onProviderEnabled(String s) {}
            @Override
            public void onProviderDisabled(String s) {}
        };
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1);
        }
        else{

            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER,30000,5, locationListener);
            Location location = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);

            if (location != null){
                updateLocationInfo(location);
            }
        }

        // JSON part from here on
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                sendToServer(longitude,latitude,byteArray);

            }
        });

    }
    //JSON object creation, to string and then send via Asyn to be done BELOW
    private void sendToServer(Double longitude, Double latitude, byte[] bmp) {
        String add = address.getText().toString();
        String num = address.getText().toString();
        String imgName = num+".JPG";
        String encodedImage = Base64.encodeToString(bmp, Base64.DEFAULT);
    }
}
