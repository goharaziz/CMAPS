package com.example.git;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.app.DownloadManager;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.graphics.Color;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkInfo;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.CookieManager;
import android.webkit.DownloadListener;
import android.webkit.URLUtil;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.RelativeLayout;
import android.widget.Toast;
import android.content.Intent;


import com.karumi.dexter.Dexter;
import com.karumi.dexter.PermissionToken;
import com.karumi.dexter.listener.PermissionDeniedResponse;
import com.karumi.dexter.listener.PermissionGrantedResponse;
import com.karumi.dexter.listener.PermissionRequest;
import com.karumi.dexter.listener.single.PermissionListener;

public class MainActivity extends AppCompatActivity {
    WebView webView;
    private String webUrl = "http://192.168.10.4:5000/";
    ProgressBar progressBarWeb;
    ProgressDialog progressDialog;
    RelativeLayout relativeLayout;
    Button btnNoInternetConnection;
    SwipeRefreshLayout swipeRefreshLayout;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Window window = getWindow();
        window.addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        webView = (WebView) findViewById(R.id.myWebView);

        progressBarWeb = (ProgressBar) findViewById(R.id.progressBar);
        progressDialog = new ProgressDialog(this);
        progressDialog.setMessage("Loading please wait");
        btnNoInternetConnection = (Button) findViewById(R.id.btnNoConnection);
        relativeLayout = (RelativeLayout) findViewById(R.id.relativeLayout);
        swipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.swipeRefreshLayout);
        swipeRefreshLayout.setColorSchemeColors(Color.BLUE,Color.YELLOW,Color.GREEN);

        swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                webView.reload();
            }
        });
        if (savedInstanceState !=null){
            webView.restoreState(savedInstanceState);
        }
        else {

            webView.getSettings().setJavaScriptEnabled(true);
            webView.getSettings().setLoadWithOverviewMode(true);
            webView.getSettings().setUseWideViewPort(true);
            webView.getSettings().setDomStorageEnabled(true);
            webView.getSettings().setLoadsImagesAutomatically(true);

            checkConnection();
        }



        webView.setDownloadListener(new DownloadListener() {
            @Override
            public void onDownloadStart(final String s, final String s1, final String s2, final String s3, long l) {
                Dexter.withActivity(MainActivity.this)
                        .withPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE)
                        .withListener(new PermissionListener() {
                            @Override
                            public void onPermissionGranted(PermissionGrantedResponse permissionGrantedResponse) {

                                DownloadManager.Request request = new DownloadManager.Request(Uri.parse(s));
                                request.setMimeType(s3);
                                String cookies = CookieManager.getInstance().getCookie(s);
                                request.addRequestHeader("cookie", cookies);
                                request.addRequestHeader("User-Agent",s1);
                                request.setDescription("Downloading File....");
                                request.setTitle(URLUtil.guessFileName(s,s2,s3));
                                request.allowScanningByMediaScanner();
                                request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
                                request.setDestinationInExternalPublicDir(
                                        Environment.DIRECTORY_DOWNLOADS, URLUtil.guessFileName(
                                                s,s2,s3));
                                DownloadManager downloadManager = (DownloadManager) getSystemService(DOWNLOAD_SERVICE);
                                downloadManager.enqueue(request);
                                Toast.makeText(MainActivity.this , "Downloading File.." , Toast.LENGTH_SHORT).show();



                            }

                            @Override
                            public void onPermissionDenied(PermissionDeniedResponse permissionDeniedResponse) {

                            }

                            @Override
                            public void onPermissionRationaleShouldBeShown(PermissionRequest permissionRequest, PermissionToken permissionToken) {
                                permissionToken.continuePermissionRequest();

                            }
                        }).check();

            }
        });

        webView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                swipeRefreshLayout.setRefreshing(false);
                super.onPageFinished(view, url);
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;

            }
        });
        webView.setWebChromeClient(new WebChromeClient(){
            @Override
            public void onProgressChanged(WebView view, int newProgress) {
                progressBarWeb.setVisibility(View.VISIBLE);
                progressBarWeb.setProgress(newProgress);

                setTitle("Loading...");
                progressDialog.show();

                if (newProgress == 100){
                    progressBarWeb.setVisibility(View.GONE);
                    setTitle(view.getTitle());
                    progressDialog.dismiss();
                }
                super.onProgressChanged(view , newProgress);
            }
        });
        btnNoInternetConnection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                checkConnection();
            }
        });
    }
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()){
            webView.goBack();
        }
        else
        {
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            builder.setMessage("Do you really want to exit")
                    .setNegativeButton("No", null)
                    .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialogInterface, int i) {
                            finishAffinity();

                        }
                    }).show();
        }

    }

    public void checkConnection() {
        ConnectivityManager connectivityManager = (ConnectivityManager)
                this.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo wifi = connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_WIFI);
        NetworkInfo mobileNetwork = connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_MOBILE);

        if (wifi.isConnected()) {
            webView.loadUrl(webUrl);

            webView.setVisibility(View.VISIBLE);
            relativeLayout.setVisibility(View.GONE);

        } else if (mobileNetwork.isConnected()) {
            webView.loadUrl(webUrl);

            webView.setVisibility(View.VISIBLE);
            relativeLayout.setVisibility(View.GONE);

        } else {
            webView.setVisibility(View.VISIBLE);
            relativeLayout.setVisibility(View.VISIBLE);
        }


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.toolbar_menu,menu);
        return super.onCreateOptionsMenu(menu);
    }




    void startwebView(){
        webView.loadUrl("https://www.punjab.gov.pk/helplines");

    }





    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()) {
            case R.id.nav_previous:
                onBackPressed();
                break;

            case R.id.nav_next:
                if (webView.canGoForward()){
                    webView.goForward();
                }
                break;

            case R.id.nav_reload:
                checkConnection();
                break;

            case R.id.nav_helpline:
                startwebView();







        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);
        webView.saveState(outState);
    }
}