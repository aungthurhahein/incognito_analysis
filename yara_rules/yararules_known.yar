// Known Keywords from experiments

rule password{
        meta:
            author="@aung"
            description="to catch password http request/response from web artifacts"
        strings:
                $a="password" nocase wide ascii
                $b={70 61 73 73 77 6f 72 64}
        condition:
                $a or $b
}

rule youtube_keywords{
        meta:
            author="@aung"
            description="youtube user activities"
        strings:
                $a="arctic monkeys" nocase wide ascii
                $b="sports animal" nocase wide ascii
                $c="bugatti veyron" nocase wide ascii
        condition: 
                any of them
}

rule ninegag_keywords{
        meta:
            author="@aung"
            description="9gag user activities"
        strings:
                $a="celebrity" nocase wide ascii
                $b="funny" nocase wide ascii
                $c="incognitofunnybot" nocase wide ascii
        condition:
                any of them
}

rule soundcloud_keywords{
        meta:
            author="@aung"
            description="soundcloud user activities"
        strings:                         
                $a="incognitomusiclover" nocase wide ascii
                $b="bleachers" nocase wide ascii
        condition:
                any of them
}

rule twitter_keywords{
        meta:
            author="@aung"
            description="twitter user activities"
        strings:            
                $a="incognitotweetbot" nocase wide ascii                
                $b="tweeted inside a nested machine" nocase wide ascii
        condition:
                any of them
}

rule amazon_keywords{
        meta:
            author="@aung"
            description="amazon user activities"
        strings:            
                $a="fire phone" nocase
                $b="no destination" nocase
                $c="amazon book" nocase
                $d="incognitobuyer"
        condition:
                any of them
}
