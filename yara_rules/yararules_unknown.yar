// Chrome Incognito Unknown keywords

// The following rules are generated with reverse engineering of classnames, data types from Chromium source code for forensic purposes.
// As for improvements of Rules Construction, fork and pull request this repo.

rule incognitomode{
        meta:
            author="@aung"                
            description="Incognito mode availability preferences."
        strings:
                $reg="IncognitoModePrefs"  wide ascii          
                $reg2="Availability"  wide ascii                
        condition:
                any of them 
}

rule Profile{
        meta:
            author="@aung"
            description="class that describes session profile information"
        strings:
                $reg="Profile"  wide ascii   
                $reg2="ProfileType"  wide ascii   
        condition:
                any of them 
}


rule OFR{
        meta:
            description="OffTheRecordProfile"
        strings:
                $reg="OffTheRecordProfileImpl"  wide ascii                
        condition:
                any of them 
}

rule IncognitoActive{
        meta:
            description="class that observe and monitor initiation of  Incognito mode"
        strings:
                $reg="WindowedIncognitoObserver"  wide ascii                
                $reg2="incognito_launched"  wide ascii                
        condition:
                any of them 
}

rule DatabaseTracker{
        meta:
            description="a tracker for opened databases connections"
        strings:
                $reg="DatabaseTracker"  wide ascii                
                $reg2="incognito_file_handles_"  wide ascii                
        condition:
                any of them 
}



